"""Index local agent-data files into FAISS using sentence-transformers.
Usage: python tools/index_embeddings.py --input-dir agent-data --out-dir agent-data/embeddings
"""
import os
import argparse
from pathlib import Path
from sentence_transformers import SentenceTransformer
import json

try:
    import faiss
except Exception:
    faiss = None

MODEL = "all-MiniLM-L6-v2"

def load_text_files(root):
    docs = []
    for p in Path(root).rglob("*.md"):
        docs.append((str(p), p.read_text(encoding='utf-8')))
    for p in Path(root).rglob("*.txt"):
        docs.append((str(p), p.read_text(encoding='utf-8')))
    for p in Path(root).rglob("*.py"):
        txt = p.read_text(encoding='utf-8')
        docs.append((str(p), txt[:5000]))
    return docs


def chunk_text(text, max_len=500):
    words = text.split()
    chunks = []
    cur = []
    for w in words:
        cur.append(w)
        if len(cur) >= max_len:
            chunks.append(" ".join(cur))
            cur = []
    if cur:
        chunks.append(" ".join(cur))
    return chunks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", default="agent-data")
    ap.add_argument("--out-dir", default="agent-data/embeddings")
    args = ap.parse_args()
    docs = load_text_files(args.input_dir)
    model = SentenceTransformer(MODEL)
    os.makedirs(args.out_dir, exist_ok=True)
    texts = []
    meta = []
    for path, content in docs:
        chunks = chunk_text(content)
        for i, c in enumerate(chunks):
            texts.append(c)
            meta.append({"source": path, "chunk": i})
    print(f"Embedding {len(texts)} chunks with {MODEL}...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    if faiss is None:
        print("faiss not available — saving embeddings as numpy + metadata")
        import numpy as np
        np.save(os.path.join(args.out_dir, 'embeddings.npy'), embeddings)
    else:
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        faiss.write_index(index, os.path.join(args.out_dir, 'faiss.index'))
    with open(os.path.join(args.out_dir, 'meta.jsonl'), 'w', encoding='utf-8') as f:
        for m in meta:
            f.write(json.dumps(m) + '\n')
    print('Indexing complete. Outputs in', args.out_dir)

if __name__ == '__main__':
    main()
