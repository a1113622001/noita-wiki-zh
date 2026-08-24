# -*- coding: utf-8 -*-
"""Noita ZH Wiki RAG query tool.
用法:
  python query.py "黑洞怎么合成"
  python query.py              # 交互模式
  python query.py "问题" --no-llm   # 只检索,不生成
"""
import argparse
import json
import math
import os
import re
import sys
import threading
import time
import urllib.request
from collections import Counter, OrderedDict, defaultdict
from typing import Any, Dict, Generator, Iterator, List, Optional, Tuple

if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE = os.path.dirname(os.path.abspath(__file__))
RAG = BASE
if os.path.exists(os.path.join(RAG, "config.json")):
    with open(os.path.join(RAG, "config.json"), encoding="utf-8") as f:
        cfg = json.load(f)
else:
    with open(os.path.join(RAG, "config.example.json"), encoding="utf-8") as f:
        cfg = json.load(f)
KEY = cfg.get("api_key") or os.environ.get("SILICONFLOW_API_KEY", "")
API = cfg["api_base"]
EMB_MODEL = cfg["embedding_model"]
RERANK_MODEL = cfg["rerank_model"]
CHAT_MODEL = cfg["chat_model"]
TOP_K = cfg.get("top_k_retrieve", 10)
TOP_N = cfg.get("top_n_rerank", 6)

import numpy as np

# Global singletons and caches
_emb = None
_chunks = None
_bm25 = None
_last_fitted_chunks_id = None


# =============================================================================
# Thread-Safe LRU Cache Implementation (R3)
# =============================================================================
class ThreadSafeLRUCache:
    """Thread-safe Least Recently Used (LRU) Cache with capacity limit and metrics."""

    def __init__(self, capacity: int = 512):
        if capacity <= 0:
            raise ValueError(f"Cache capacity must be positive, got {capacity}")
        self.capacity = capacity
        self._cache: OrderedDict = OrderedDict()
        self._lock = threading.RLock()
        self._hits = 0
        self._misses = 0

    def get(self, key: str) -> Optional[Any]:
        with self._lock:
            if key not in self._cache:
                self._misses += 1
                return None
            self._cache.move_to_end(key)
            self._hits += 1
            return self._cache[key]

    def put(self, key: str, value: Any) -> None:
        with self._lock:
            if key in self._cache:
                self._cache.move_to_end(key)
                self._cache[key] = value
                return
            if len(self._cache) >= self.capacity:
                self._cache.popitem(last=False)  # Evict oldest entry (LRU)
            self._cache[key] = value

    def set(self, key: str, value: Any) -> None:
        self.put(key, value)

    def clear(self) -> None:
        with self._lock:
            self._cache.clear()
            self._hits = 0
            self._misses = 0

    def get_stats(self) -> Dict[str, Any]:
        with self._lock:
            total = self._hits + self._misses
            hit_rate = (self._hits / total) if total > 0 else 0.0
            return {
                "size": len(self._cache),
                "capacity": self.capacity,
                "hits": self._hits,
                "misses": self._misses,
                "hit_rate": round(hit_rate, 4),
            }

    def stats(self) -> Dict[str, Any]:
        return self.get_stats()

    def __len__(self) -> int:
        with self._lock:
            return len(self._cache)

    def __contains__(self, key: str) -> bool:
        with self._lock:
            return key in self._cache


_emb_cache = ThreadSafeLRUCache(capacity=1024)
_query_cache = ThreadSafeLRUCache(capacity=512)


def clear_caches() -> None:
    """Clear all in-memory LRU caches."""
    global _last_fitted_chunks_id, _bm25
    _emb_cache.clear()
    _query_cache.clear()
    _last_fitted_chunks_id = None
    _bm25 = None


def get_cache_stats() -> Dict[str, Any]:
    """Retrieve runtime telemetry for all LRU caches."""
    return {
        "embedding_cache": _emb_cache.get_stats(),
        "query_cache": _query_cache.get_stats(),
    }


# =============================================================================
# Defensive Utilities & Vector Embedder
# =============================================================================
def _check_lfs(file_path: str, name: Optional[str] = None) -> None:
    """Check if file is a Git LFS pointer file and provide actionable instructions."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    name = name or os.path.basename(file_path)
    try:
        if os.path.getsize(file_path) < 1024:
            with open(file_path, "rb") as f:
                header = f.read(100)
            if b"version https://git-lfs.github.com/spec/v1" in header or b"oid sha256:" in header:
                raise RuntimeError(
                    f"检测到 {name} 是 Git LFS 指针文件而非真实数据文件！\n"
                    f"请安装 Git LFS 并执行以下命令拉取真实数据:\n"
                    f"    git lfs install\n"
                    f"    git lfs pull\n"
                    f"或者重新运行 `python rag/build_index.py` 构建索引。"
                )
    except (RuntimeError, FileNotFoundError):
        raise
    except Exception:
        pass


def get_embedder() -> Dict[str, np.ndarray]:
    """Load vector matrix with Git LFS check and L2 pre-normalization."""
    global _emb
    if _emb is None:
        index_path = os.path.join(RAG, "index.npy")
        _check_lfs(index_path, "index.npy")
        m = np.load(index_path).astype(np.float32)
        norms = np.linalg.norm(m, axis=1, keepdims=True)
        norms[norms == 0] = 1e-9
        m_norm = m / norms
        _emb = {"m": m_norm}
    return _emb


def post(path: str, body: dict, retries: int = 5, timeout: int = 180) -> dict:
    """Synchronous HTTP POST to API endpoint with exponential retry."""
    url = API + path
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(body).encode("utf-8"),
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except Exception as e:
            last = e
            print(f"  API 调用失败({path}): {e!r}, 重试 {i+1}", file=sys.stderr)
            time.sleep(2 + 2 * i)
    raise last


def post_stream(path: str, body: dict, retries: int = 3, timeout: int = 60) -> Generator[str, None, None]:
    """Execute streaming HTTP POST and yield SSE delta content tokens (R1)."""
    url = API + path
    payload = dict(body)
    payload["stream"] = True
    data_bytes = json.dumps(payload).encode("utf-8")

    last_err = None
    for attempt in range(retries):
        yielded_any = False
        try:
            req = urllib.request.Request(
                url,
                data=data_bytes,
                headers={
                    "Authorization": f"Bearer {KEY}",
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream"
                }
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                for raw_line in resp:
                    line = raw_line.decode("utf-8").strip()
                    if not line or line.startswith(":"):
                        continue
                    if line.startswith("data:"):
                        data_part = line[5:].strip()
                        if data_part == "[DONE]":
                            break
                        try:
                            chunk = json.loads(data_part)
                            choices = chunk.get("choices", [])
                            if choices:
                                delta = choices[0].get("delta", {})
                                content = delta.get("content", "")
                                if content:
                                    yielded_any = True
                                    yield content
                        except json.JSONDecodeError:
                            continue
                return
        except Exception as e:
            last_err = e
            if yielded_any:
                print(f"\n[警告] 流式输出中断: {e!r}", file=sys.stderr)
                raise
            if attempt < retries - 1:
                time.sleep(1 + attempt)
            else:
                raise last_err


def embed_one(text: str, use_cache: bool = True) -> List[float]:
    """Compute query embedding vector with LRU caching."""
    key = text.strip().lower()
    if use_cache:
        cached = _emb_cache.get(key)
        if cached is not None:
            return cached

    d = post("/embeddings", {"model": EMB_MODEL, "input": [text], "encoding_format": "float"})
    emb = d["data"][0]["embedding"]

    if use_cache:
        _emb_cache.put(key, emb)
    return emb


# =============================================================================
# Pure Python Zero-Dependency BM25 Retriever & Tokenizer (R2)
# =============================================================================
def tokenize(text: str) -> List[str]:
    """Pure Python multi-lingual tokenizer for Noita Wiki terms.
    - Captures alphanumeric identifiers, spells, codes, numbers, dotted floats, and Finnish/Latin diacritics.
    - Decomposes Chinese text into character unigrams and bigrams without external dependencies.
    """
    if not text:
        return []
    text = text.lower()
    tokens = []

    # Alphanumeric words, spell IDs, code components, numbers, decimals, diacritics
    for word in re.findall(r"[a-z0-9_\u00c0-\u024f]+(?:\.[a-z0-9_\u00c0-\u024f]+)*", text):
        tokens.append(word)
        if "_" in word:
            for part in word.split("_"):
                if part:
                    tokens.append(part)
        if "." in word:
            for part in word.split("."):
                if part:
                    tokens.append(part)

    # Chinese unigrams and bigrams
    for zh_seq in re.findall(r"[\u4e00-\u9fff]+", text):
        n = len(zh_seq)
        for i in range(n):
            tokens.append(zh_seq[i])
            if i + 1 < n:
                tokens.append(zh_seq[i : i + 2])

    return tokens


class BM25Retriever:
    """Zero-dependency Inverted Index & Okapi BM25 ranking engine with title boosting."""

    def __init__(
        self,
        k1: float = 1.5,
        b: float = 0.75,
        title_weight: float = 4.0,
        ctx_weight: float = 2.0,
    ):
        self.k1 = k1
        self.b = b
        self.title_weight = title_weight
        self.ctx_weight = ctx_weight
        self.corpus_size = 0
        self.avgdl = 0.0
        self.doc_lengths: List[int] = []
        self.postings: Dict[str, List[Tuple[int, float]]] = defaultdict(list)
        self.doc_freqs: Dict[str, int] = defaultdict(int)
        self.idf: Dict[str, float] = {}
        self.title_exact_map: Dict[str, List[int]] = defaultdict(list)

    def fit(self, chunks: List[dict]) -> None:
        """Build inverted index, IDF tables, and title exact hash index from chunks."""
        self.corpus_size = len(chunks)
        self.doc_lengths = []
        self.postings = defaultdict(list)
        self.doc_freqs = defaultdict(int)
        self.idf = {}
        self.title_exact_map = defaultdict(list)
        total_len = 0

        # Load title_to_file.json if available
        title_file_map = {}
        parent_dir = os.path.dirname(BASE)
        title_json_candidates = [
            os.path.join(parent_dir, "title_to_file.json"),
            os.path.join(BASE, "title_to_file.json"),
            os.path.join(os.getcwd(), "title_to_file.json"),
        ]
        for p in title_json_candidates:
            if os.path.exists(p):
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        title_file_map = json.load(f)
                    break
                except Exception:
                    pass

        file_to_docs = defaultdict(list)

        for doc_id, c in enumerate(chunks):
            title = c.get("title", "")
            ctx = c.get("ctx", "")
            text = c.get("text", "")
            file_name = c.get("file", "")

            if file_name:
                file_to_docs[file_name.lower()].append(doc_id)
                if file_name.endswith(".md"):
                    file_to_docs[file_name[:-3].lower()].append(doc_id)

            clean_title = title.strip().lower()
            if clean_title:
                self.title_exact_map[clean_title].append(doc_id)

            title_tokens = tokenize(title)
            ctx_tokens = tokenize(ctx)
            text_tokens = tokenize(text)

            counts = Counter(text_tokens)
            for t in ctx_tokens:
                counts[t] += self.ctx_weight
            for t in title_tokens:
                counts[t] += self.title_weight

            doc_len = len(text_tokens) + len(ctx_tokens) + len(title_tokens)
            self.doc_lengths.append(doc_len)
            total_len += doc_len

            for t, tf in counts.items():
                self.postings[t].append((doc_id, tf))
                self.doc_freqs[t] += 1

        # Link alias titles from title_to_file.json
        if title_file_map:
            for alias_title, target_file in title_file_map.items():
                alias_clean = alias_title.strip().lower()
                target_clean = target_file.lower()
                for doc_id in file_to_docs.get(target_clean, []):
                    if doc_id not in self.title_exact_map[alias_clean]:
                        self.title_exact_map[alias_clean].append(doc_id)
                if not target_clean.endswith(".md"):
                    for doc_id in file_to_docs.get(target_clean + ".md", []):
                        if doc_id not in self.title_exact_map[alias_clean]:
                            self.title_exact_map[alias_clean].append(doc_id)

        self.avgdl = (total_len / self.corpus_size) if self.corpus_size > 0 else 0.0

        for t, df in self.doc_freqs.items():
            self.idf[t] = math.log((self.corpus_size - df + 0.5) / (df + 0.5) + 1.0)

    def search(self, query: str, top_k: int = 10) -> Tuple[np.ndarray, np.ndarray]:
        """Search inverted index with Okapi BM25 and exact title matching boost."""
        query_tokens = tokenize(query)
        clean_q = query.strip().lower()
        exact_title_matches = set(self.title_exact_map.get(clean_q, []))

        if not query_tokens and not exact_title_matches:
            return np.array([], dtype=int), np.array([], dtype=np.float32)

        scores = defaultdict(float)
        token_counts = Counter(query_tokens)

        for qt, q_freq in token_counts.items():
            idf = self.idf.get(qt)
            if idf is None:
                continue
            for doc_id, tf in self.postings.get(qt, []):
                dl = self.doc_lengths[doc_id]
                denom = tf + self.k1 * (1.0 - self.b + self.b * (dl / (self.avgdl or 1.0)))
                term_score = idf * (tf * (self.k1 + 1.0)) / (denom or 1e-9)
                scores[doc_id] += term_score * q_freq

        for doc_id in exact_title_matches:
            scores[doc_id] += 15.0

        if not scores:
            return np.array([], dtype=int), np.array([], dtype=np.float32)

        sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
        idx = np.array([doc_id for doc_id, _ in sorted_items], dtype=int)
        sims = np.array([score for _, score in sorted_items], dtype=np.float32)
        return idx, sims


def get_bm25_retriever() -> BM25Retriever:
    """Lazy singleton loader for BM25 inverted index."""
    global _bm25, _last_fitted_chunks_id
    chunks = load_chunks()
    chunks_fingerprint = (id(chunks), len(chunks), id(chunks[0]) if chunks else 0)
    if _bm25 is None or _last_fitted_chunks_id != chunks_fingerprint:
        _bm25 = BM25Retriever()
        _bm25.fit(chunks)
        _last_fitted_chunks_id = chunks_fingerprint
    return _bm25


# =============================================================================
# Retrieval & Hybrid RRF Engine (R2)
# =============================================================================
def search_knowledge_dense(
    query: str, k: int = 10, use_cache: bool = True
) -> Tuple[np.ndarray, np.ndarray]:
    """Dense vector retrieval via BGE-M3 embeddings."""
    q = np.array(embed_one(query, use_cache=use_cache), dtype=np.float32)
    q_norm = np.linalg.norm(q)
    if q_norm > 0:
        q = q / q_norm
    m = get_embedder()["m"]
    sims = m @ q
    idx = np.argsort(sims)[::-1][:k]
    return idx, sims[idx]


def search_knowledge_bm25(query: str, k: int = 10) -> Tuple[np.ndarray, np.ndarray]:
    """Sparse full-text retrieval via BM25 with title weighting."""
    retriever = get_bm25_retriever()
    return retriever.search(query, top_k=k)


def rrf_fuse(
    dense_idx: Optional[np.ndarray],
    dense_scores: Optional[np.ndarray],
    bm25_idx: Optional[np.ndarray],
    bm25_scores: Optional[np.ndarray],
    top_k: int = 10,
    rrf_k: int = 60,
    w_dense: float = 1.0,
    w_bm25: float = 1.0,
) -> Tuple[np.ndarray, np.ndarray]:
    """Reciprocal Rank Fusion combiner."""
    fused_scores = defaultdict(float)
    if dense_idx is not None and len(dense_idx) > 0:
        for rank, doc_id in enumerate(dense_idx, 1):
            fused_scores[int(doc_id)] += w_dense / (rrf_k + rank)
    if bm25_idx is not None and len(bm25_idx) > 0:
        for rank, doc_id in enumerate(bm25_idx, 1):
            fused_scores[int(doc_id)] += w_bm25 / (rrf_k + rank)

    if not fused_scores:
        return np.array([], dtype=int), np.array([], dtype=np.float32)

    sorted_items = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    idx = np.array([doc_id for doc_id, _ in sorted_items], dtype=int)
    sims = np.array([score for _, score in sorted_items], dtype=np.float32)
    return idx, sims


def search_knowledge_hybrid(
    query: str,
    k: int = 10,
    rrf_k: int = 60,
    w_dense: float = 1.0,
    w_bm25: float = 1.0,
    use_cache: bool = True,
) -> Tuple[np.ndarray, np.ndarray]:
    """Hybrid dense + sparse retrieval with RRF ranking."""
    try:
        d_idx, d_sims = search_knowledge_dense(query, k=k, use_cache=use_cache)
    except Exception:
        # Fallback to BM25 if dense embedding fails (offline or API issue)
        return search_knowledge_bm25(query, k=k)

    b_idx, b_sims = search_knowledge_bm25(query, k=k)
    return rrf_fuse(
        d_idx,
        d_sims,
        b_idx,
        b_sims,
        top_k=k,
        rrf_k=rrf_k,
        w_dense=w_dense,
        w_bm25=w_bm25,
    )


def retrieve(
    query: str, k: int = 10
) -> Tuple[np.ndarray, np.ndarray]:
    """Primary retrieval entry point preserving 100% backward compatibility."""
    if not KEY:
        return search_knowledge_bm25(query, k=k)
    return search_knowledge_hybrid(query, k=k)


# =============================================================================
# Noise Filtering, Reranking & Corpus Loading
# =============================================================================
def _noise(c: dict) -> bool:
    """过滤无信息量的块:空链接/图标行/过短/全是图片"""
    t = c.get("text", "")
    if len(t) < 40:
        return True
    if t.count("](") > 8 and re.search(r"\[\]\([^)]*\.md\)", t):
        # 大段空文本链接(模板图标排布)
        empty_links = len(re.findall(r"\[\]\([^)]*\.md\)", t))
        if empty_links >= 3:
            return True
    if t.count("![") > 4:  # 纯图片画廊
        return True
    return False


def rerank(query: str, docs: List[str], top_n: int = TOP_N) -> List[dict]:
    """Rerank candidates and return sorted results in descending order of relevance_score."""
    d = post(
        "/rerank",
        {"model": RERANK_MODEL, "query": query, "documents": docs, "top_n": top_n},
    )
    results = sorted(d["results"], key=lambda x: x.get("relevance_score", 0.0), reverse=True)
    return results[:top_n]  # [{index, relevance_score}]


def load_chunks() -> List[dict]:
    """Lazy singleton loader for chunks.json."""
    global _chunks
    if _chunks is None:
        chunks_path = os.path.join(RAG, "chunks.json")
        _check_lfs(chunks_path, "chunks.json")
        with open(chunks_path, encoding="utf-8") as f:
            _chunks = json.load(f)
    return _chunks


# =============================================================================
# Generation & Unified Answering (R1, R2, R3)
# =============================================================================
def chat(
    messages: List[dict], max_tokens: int = 1024, stream: bool = False
) -> Any:
    """Call chat completions API supporting both blocking and streaming modes."""
    body = {
        "model": CHAT_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }
    if not stream:
        d = post("/chat/completions", body)
        return d["choices"][0]["message"]["content"]
    else:
        return post_stream("/chat/completions", body)


SYSTEM_PROMPT = """你是 Noita(游戏)中文 Wiki 知识库助手。请基于提供的知识库片段回答用户问题。
规则:
1. 只依据提供的片段回答,不要编造;片段不足时明确说明"知识库中没有找到相关内容"。
2. 回答用简体中文,尽量准确、具体,可以引用片段中的游戏机制细节。
3. 片段末尾会标注 [来源: 页面标题 | 文件名],回答涉及关键事实时在句末附上来源。"""


def answer(
    query: str,
    no_llm: bool = False,
    k: int = 10,
    top_n: int = TOP_N,
    stream: bool = False,
    use_cache: bool = True,
) -> Tuple[Any, List[dict], List[float]]:
    """Answer question with strictly aligned scores, caching, and streaming support."""
    chunks = load_chunks()

    # Detect if chunks singleton was replaced (e.g. mocked in unit tests)
    global _last_fitted_chunks_id
    chunks_fingerprint = (id(chunks), len(chunks), id(chunks[0]) if chunks else 0)
    if _last_fitted_chunks_id is not None and _last_fitted_chunks_id != chunks_fingerprint:
        _query_cache.clear()
        if _bm25 is not None:
            _bm25.fit(chunks)
    _last_fitted_chunks_id = chunks_fingerprint

    cache_key = f"{query.strip().lower()}##{int(no_llm)}##{k}##{top_n}"

    # 1. Check Query Cache
    if use_cache:
        cached = _query_cache.get(cache_key)
        if cached is not None:
            cached_ans, cached_picked, cached_sims = cached
            if stream and cached_ans is not None:
                def _stream_cached():
                    chunk_sz = 4
                    for i in range(0, len(cached_ans), chunk_sz):
                        yield cached_ans[i : i + chunk_sz]
                return _stream_cached(), list(cached_picked), list(cached_sims)
            return cached_ans, list(cached_picked), list(cached_sims)

    # 2. Retrieval & Noise Filtering
    idx, sims = retrieve(query, k)
    cand_pairs = [(chunks[i], float(s)) for i, s in zip(idx, sims) if not _noise(chunks[i])]
    if len(cand_pairs) < top_n:
        extra_pairs = [(chunks[i], float(s)) for i, s in zip(idx, sims) if _noise(chunks[i])]
        cand_pairs.extend(extra_pairs)
    cand_pairs = cand_pairs[:k]

    cand = [c for c, _ in cand_pairs]
    cand_sims = [s for _, s in cand_pairs]
    docs = [f"[来源: {c['title']} | {c['file']}]\n{c['ctx']}\n{c['text']}" for c in cand]

    # 3. LLM Mode vs Retrieval-only Mode
    if not no_llm:
        rr = rerank(query, docs, top_n)
        picked = [cand[r["index"]] for r in rr]
        picked_sims = [cand_sims[r["index"]] for r in rr]
        context = "\n\n---\n\n".join(
            f"[来源: {c['title']} | {c['file']}]\n{c['ctx']}\n{c['text']}" for c in picked
        )
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"知识库片段:\n{context}\n\n问题:{query}"},
        ]

        if not stream:
            ans = chat(messages)
            if use_cache:
                _query_cache.put(cache_key, (ans, picked, picked_sims))
            return ans, picked, picked_sims
        else:
            raw_stream = chat(messages, stream=True)

            def _wrapper():
                tokens = []
                try:
                    for t in raw_stream:
                        tokens.append(t)
                        yield t
                finally:
                    if tokens and use_cache:
                        full_ans = "".join(tokens)
                        _query_cache.put(cache_key, (full_ans, picked, picked_sims))

            return _wrapper(), picked, picked_sims

    # 只检索: 返回 top_n 片段及对齐的分数
    res_picked = cand[:top_n]
    res_sims = cand_sims[:top_n]
    if use_cache:
        _query_cache.put(cache_key, (None, res_picked, res_sims))
    return None, res_picked, res_sims


# =============================================================================
# CLI Typewriter Presentation & Entry Points (R1)
# =============================================================================
def run(q: str, args: Any) -> None:
    """Execute CLI query with real-time typewriter token streaming and citations."""
    t0 = time.time()
    stream_mode = not getattr(args, "no_llm", False) and not getattr(args, "no_stream", False)
    k_val = getattr(args, "k", 10)
    top_n_val = getattr(args, "top_n", TOP_N)
    try:
        ans, picked, sims = answer(
            q,
            no_llm=args.no_llm,
            k=k_val,
            top_n=top_n_val,
            stream=stream_mode,
        )
    except Exception as e:
        print(f"错误: {e!r}", file=sys.stderr)
        return

    if args.no_llm or ans is None:
        if not args.no_llm and not KEY:
            print("[提示] 未配置 API Key，已自动降级为本地离线检索模式。")
        print(f"\n=== 检索结果 (用时 {time.time()-t0:.3f}s) ===\n")
        for i, c in enumerate(picked, 1):
            sim_val = sims[i - 1] if i - 1 < len(sims) else 0.0
            print(f"[{i}] (相似度 {sim_val:.3f}) {c['title']} | {c['file']}")
            print(f"    {c.get('text', '')[:200]}\n")
    else:
        print("\n=== 回答 ===\n")
        if hasattr(ans, "__iter__") and not isinstance(ans, (str, bytes)):
            first_token = True
            ttft = None
            for token in ans:
                if first_token:
                    ttft = time.time() - t0
                    first_token = False
                sys.stdout.write(token)
                sys.stdout.flush()
            print()
            if ttft is not None:
                print(f"\n(首字延迟 TTFT: {ttft*1000:.0f}ms | 总用时 {time.time()-t0:.2f}s)")
        else:
            print(ans)
            print(f"\n(总用时 {time.time()-t0:.2f}s)")

        print("\n--- 引用来源 ---")
        for i, c in enumerate(picked, 1):
            ctx_snip = c.get("ctx", "")[:60]
            print(f"[{i}] {c['title']} | {c['file']} | {ctx_snip}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Noita Wiki RAG")
    ap.add_argument("question", nargs="?", help="问题")
    ap.add_argument("--no-llm", action="store_true", help="只检索不生成")
    ap.add_argument("--no-stream", action="store_true", help="禁用流式输出")
    ap.add_argument("--k", type=int, default=TOP_K)
    ap.add_argument("--top-n", type=int, default=TOP_N)
    args = ap.parse_args()

    if args.question:
        run(args.question, args)
    else:
        print("Noita Wiki RAG 交互模式(输入 exit 退出)\n")
        while True:
            try:
                q = input("> ").strip()
            except EOFError:
                break
            if not q:
                continue
            if q.lower() in ("exit", "quit"):
                break
            run(q, args)


if __name__ == "__main__":
    main()
