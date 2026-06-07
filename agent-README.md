ECO — Personal AI agent for Brian Kennedy Jr

This folder contains agent-data and tools to index and run ECO locally using private models:

- LLM: Local Llama 2-family model (via llama.cpp or llama-cpp-python)
- Embeddings: sentence-transformers (all-MiniLM-L6-v2) to create FAISS index
- STT: Whisper local (openai/whisper or whisper.cpp)
- TTS: Coqui TTS or other local TTS engines

Quick steps:
1. Install requirements: python -m pip install -r tools/requirements-agent.txt
2. Run: python tools/index_embeddings.py --input-dir agent-data --out-dir agent-data/embeddings
3. Start agent server: python tools/agent_server.py

Security: This setup keeps data local; do not commit private API keys.
