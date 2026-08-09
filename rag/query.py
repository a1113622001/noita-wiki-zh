# -*- coding: utf-8 -*-
"""Noita ZH Wiki RAG query tool.
用法:
  python query.py "黑洞怎么合成"
  python query.py              # 交互模式
  python query.py "问题" --no-llm   # 只检索,不生成
"""
import argparse, json, os, sys, time, urllib.request, re

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
TOP_K = cfg["top_k_retrieve"]
TOP_N = cfg["top_n_rerank"]

import numpy as np
_emb = None
def get_embedder():
    global _emb
    if _emb is None:
        _emb = {"m": np.load(os.path.join(RAG, "index.npy"))}
    return _emb

def post(path, body, retries=5, timeout=180):
    url = API + path
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.load(r)
        except Exception as e:
            last = e
            print(f"  API 调用失败({path}): {e!r}, 重试 {i+1}", file=sys.stderr)
            time.sleep(2 + 2 * i)
    raise last

def embed_one(text):
    d = post("/embeddings", {"model": EMB_MODEL, "input": [text], "encoding_format": "float"})
    return d["data"][0]["embedding"]

def retrieve(query, k=TOP_K):
    q = np.array(embed_one(query), dtype=np.float32)
    m = get_embedder()["m"]
    # 余弦相似度
    norms = np.linalg.norm(m, axis=1)
    sims = (m @ q) / (norms * np.linalg.norm(q) + 1e-9)
    idx = np.argsort(sims)[::-1][:k]
    return idx, sims[idx]

def _noise(c):
    """过滤无信息量的块:空链接/图标行/过短/全是图片"""
    t = c["text"]
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

def rerank(query, docs, top_n=TOP_N):
    d = post("/rerank", {"model": RERANK_MODEL, "query": query,
                         "documents": docs, "top_n": top_n})
    results = sorted(d["results"], key=lambda x: x["index"])
    return results  # [{index, relevance_score}]

def load_chunks():
    with open(os.path.join(RAG, "chunks.json"), encoding="utf-8") as f:
        return json.load(f)

def chat(messages, max_tokens=1024):
    d = post("/chat/completions", {"model": CHAT_MODEL, "messages": messages,
                                   "max_tokens": max_tokens, "temperature": 0.3})
    return d["choices"][0]["message"]["content"]

SYSTEM_PROMPT = """你是 Noita(游戏)中文 Wiki 知识库助手。请基于提供的知识库片段回答用户问题。
规则:
1. 只依据提供的片段回答,不要编造;片段不足时明确说明"知识库中没有找到相关内容"。
2. 回答用简体中文,尽量准确、具体,可以引用片段中的游戏机制细节。
3. 片段末尾会标注 [来源: 页面标题 | 文件名],回答涉及关键事实时在句末附上来源。"""

def answer(query, no_llm=False, k=TOP_K, top_n=TOP_N):
    chunks = load_chunks()
    idx, sims = retrieve(query, k)
    # 过滤噪声块后再 rerank
    cand = [chunks[i] for i in idx if not _noise(chunks[i])]
    while len(cand) < top_n:
        # 噪声太多导致候选不足时放宽
        extra = [chunks[i] for i in idx if _noise(chunks[i])]
        cand += extra
        break
    cand = cand[:k]
    docs = [f"[来源: {c['title']} | {c['file']}]\n{c['ctx']}\n{c['text']}" for c in cand]
    if not no_llm:
        rr = rerank(query, docs, top_n)
        picked = [cand[r["index"]] for r in rr]
        context = "\n\n---\n\n".join(
            f"[来源: {c['title']} | {c['file']}]\n{c['ctx']}\n{c['text']}" for c in picked)
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"知识库片段:\n{context}\n\n问题:{query}"},
        ]
        ans = chat(messages)
        return ans, picked, sims
    # 只检索:返回 top_n 片段
    return None, cand[:top_n], sims

def main():
    ap = argparse.ArgumentParser(description="Noita Wiki RAG")
    ap.add_argument("question", nargs="?", help="问题")
    ap.add_argument("--no-llm", action="store_true", help="只检索不生成")
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

def run(q, args):
    t0 = time.time()
    try:
        ans, picked, sims = answer(q, no_llm=args.no_llm, k=args.k, top_n=args.top_n)
    except Exception as e:
        print(f"错误: {e!r}", file=sys.stderr)
        return
    print(f"\n=== 回答 (用时 {time.time()-t0:.1f}s) ===\n")
    if args.no_llm:
        for i, c in enumerate(picked, 1):
            print(f"[{i}] (相似度 {sims[i-1]:.3f}) {c['title']} | {c['file']}")
            print(f"    {c['text'][:200]}\n")
    else:
        print(ans)
        print("\n--- 引用来源 ---")
        for i, c in enumerate(picked, 1):
            print(f"[{i}] {c['title']} | {c['file']} | {c['ctx'][:60]}")

if __name__ == "__main__":
    main()
