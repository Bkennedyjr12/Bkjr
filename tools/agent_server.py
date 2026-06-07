"""Minimal FastAPI server skeleton for ECO.
- Loads embeddings from agent-data/embeddings
- Exposes /query to run a semantic search + local LLM call (placeholder)
"""
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title='ECO Agent')

class Query(BaseModel):
    q: str

@app.post('/query')
async def query(q: Query):
    # Placeholder: load FAISS and metadata, run semantic search, then call local LLM
    return {"answer": "This is a demo response. Replace with local LLM call."}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8787)
