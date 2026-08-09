# -*- coding: utf-8 -*-
"""Build vector index for Noita ZH wiki knowledge base (resumable).
Stage 1: pages/*.md -> chunks.json
Stage 2: embed chunks -> vectors.bin (append) -> index.npy
Re-running resumes from where it left off.
"""
import json, os, re, sys, time, urllib.request, hashlib

BASE = r"C:/Users/baiyec/AppData/Roaming/reasonix/global-workspace/noita-wiki-zh"
PAGES = os.path.join(BASE, "pages")
RAG = os.path.join(BASE, "rag")
os.makedirs(RAG, exist_ok=True)

if os.path.exists(os.path.join(RAG, "config.json")):
    with open(os.path.join(RAG, "config.json"), encoding="utf-8") as f:
        cfg = json.load(f)
else:
    with open(os.path.join(RAG, "config.example.json"), encoding="utf-8") as f:
        cfg = json.load(f)
KEY = cfg.get("api_key") or os.environ.get("SILICONFLOW_API_KEY", "")
API = "https://api.siliconflow.cn/v1"
EMB_MODEL = cfg.get("embedding_model", "BAAI/bge-m3")
BATCH = 16
MAX_CHUNK = 1000
MAX_CHUNK_HARD = 1600
CHUNKS_JSON = os.path.join(RAG, "chunks.json")
BIN = os.path.join(RAG, "vectors.bin")
INDEX_NPY = os.path.join(RAG, "index.npy")

def post(path, body, retries=6):
    url = API + path
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"),
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except Exception as e:
            last = e
            time.sleep(3 + 3 * i)
    raise last

def embed_batch(texts):
    d = post("/embeddings", {"model": EMB_MODEL, "input": texts, "encoding_format": "float"})
    rows = sorted(d["data"], key=lambda x: x["index"])
    return [r["embedding"] for r in rows]

def chunk_markdown(text, page_title):
    lines = text.split("\n")
    chunks = []
    cur_chain = []
    cur = []
    def flush():
        if not cur:
            return
        body = "\n".join(cur).strip()
        if body:
            chunks.append((list(cur_chain), body))
        cur.clear()
    for ln in lines:
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            flush()
            level = len(m.group(1))
            title = m.group(2).strip()
            while len(cur_chain) >= level:
                cur_chain.pop()
            cur_chain.append(title)
            cur.append(ln)
        else:
            cur.append(ln)
    flush()
    merged = []
    for chain, body in chunks:
        if merged and len(body) <= 200 and len(merged[-1][1]) + len(body) < MAX_CHUNK_HARD:
            merged[-1] = (merged[-1][0], merged[-1][1] + "\n" + body)
        else:
            merged.append((chain, body))
    final = []
    for chain, body in merged:
        while len(body) > MAX_CHUNK_HARD:
            cut = body.rfind("。", 0, MAX_CHUNK)
            if cut < 200:
                cut = body.rfind(" ", 0, MAX_CHUNK)
            if cut < 200:
                cut = MAX_CHUNK
            final.append((chain, body[:cut]))
            body = body[cut:].lstrip()
        if body:
            final.append((chain, body))
    out = []
    for chain, body in final:
        ctx = page_title
        for h in chain:
            ctx += " > " + h
        out.append({"ctx": ctx, "text": body})
    return out

def stage1():
    with open(os.path.join(BASE, "title_to_file.json"), encoding="utf-8") as f:
        t2f = json.load(f)
    file2title = {v: k for k, v in t2f.items()}
    all_chunks = []
    files = sorted(f for f in os.listdir(PAGES) if f.endswith(".md"))
    for fi, fn in enumerate(files):
        with open(os.path.join(PAGES, fn), encoding="utf-8") as f:
            text = f.read()
        title = file2title.get(fn, fn[:-3])
        if "本页面是重定向页" in text[:200]:
            continue
        text = re.sub(r"\*\*来源:\*\*[^\n]*\n", "", text)
        text = re.sub(r"\*\*分类:\*\*[^\n]*\n", "", text)
        for c in chunk_markdown(text, title):
            cid = hashlib.md5((title + c["text"]).encode()).hexdigest()[:16]
            all_chunks.append({"id": cid, "file": fn, "title": title,
                               "ctx": c["ctx"], "text": c["text"]})
        if (fi + 1) % 500 == 0:
            print(f"chunked {fi+1}/{len(files)}, chunks {len(all_chunks)}", flush=True)
    with open(CHUNKS_JSON, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False)
    print(f"stage1 done: {len(all_chunks)} chunks -> {CHUNKS_JSON}", flush=True)
    return all_chunks

def stage2(chunks):
    import numpy as np
    dim = 1024
    done = 0
    if os.path.exists(BIN):
        size = os.path.getsize(BIN)
        done = size // (dim * 4)
        print(f"resume: {done} already embedded", flush=True)
    n = len(chunks)
    t0 = time.time()
    with open(BIN, "ab") as fb:
        i = done
        while i < n:
            batch = [c["ctx"] + "\n" + c["text"] for c in chunks[i:i + BATCH]]
            vecs = None
            for attempt in range(6):
                try:
                    vecs = embed_batch(batch)
                    break
                except Exception as e:
                    print(f"  batch {i} error {e!r} retry {attempt+1}", flush=True)
                    time.sleep(4)
            if vecs is None:
                raise RuntimeError(f"batch {i} failed after retries")
            fb.write(np.array(vecs, dtype=np.float32).tobytes())
            fb.flush()
            i += len(batch)
            if (i // BATCH) % 20 == 0:
                print(f"embedded {i}/{n} elapsed={time.time()-t0:.0f}s", flush=True)
    mat = np.fromfile(BIN, dtype=np.float32).reshape(n, dim)
    np.save(INDEX_NPY, mat)
    os.remove(BIN)
    print(f"stage2 done: {n} x {dim} -> {INDEX_NPY} "
          f"({os.path.getsize(INDEX_NPY)/1024/1024:.1f} MB) elapsed={time.time()-t0:.0f}s", flush=True)

def main():
    chunks = stage1() if not os.path.exists(CHUNKS_JSON) else json.load(open(CHUNKS_JSON, encoding="utf-8"))
    stage2(chunks)

if __name__ == "__main__":
    main()
