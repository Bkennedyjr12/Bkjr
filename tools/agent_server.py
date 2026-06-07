from fastapi import FastAPI
from pydantic import BaseModel
import os
import json

app = FastAPI(title='ECO Agent')

class Query(BaseModel):
    q: str

# Lightweight semantic search using sentence-transformers + numpy fallback
EMB_DIR = os.path.join('agent-data','embeddings')
try:
    import numpy as np
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception:
    model = None

# Load precomputed embeddings if available
meta = []
embeddings = None

if os.path.isdir(EMB_DIR):
    meta_path = os.path.join(EMB_DIR,'meta.jsonl')
    emb_npy = os.path.join(EMB_DIR,'embeddings.npy')
    if os.path.isfile(meta_path) and os.path.isfile(emb_npy):
        with open(meta_path,'r',encoding='utf-8') as f:
            meta = [json.loads(l) for l in f]
        embeddings = np.load(emb_npy)

@app.post('/query')
async def query(q: Query):
    # If we have embeddings, run semantic search and return top contexts
    if embeddings is not None and model is not None:
        qv = model.encode([q.q])[0]
        # cosine similarity
        import numpy as np
        sims = embeddings @ qv
        idx = np.argsort(-sims)[:4]
        results = []
        for i in idx:
            m = meta[i]
            results.append({'source': m.get('source'), 'chunk': m.get('chunk'), 'score': float(sims[i])})
        return {'answer': 'Top matches returned', 'matches': results}
    # Fallback demo response
    return {'answer': 'ECO demo: no embeddings available yet. Run tools/index_embeddings.py to index agent-data.'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8787)
