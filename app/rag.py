from sentence_transformers import SentenceTransformer
import numpy as np
from .utils import extract_text, chunk_text
from .vector_store import FaissStore
from .llm import build_prompt,call_llm

class RAGBot():
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.store = FaissStore(dim=384)

    def index_pdf(self, filepath, source):
        with open(filepath, "rb") as f:
            text  = extract_text(f)

        chunks = chunk_text(text)
        embeddings = self.embedder.encode(chunks).astype(np.float32)

        metas = [{"source": source, "text":chunk} for chunk in chunks]

        self.store.add(embeddings, metas)
        self.store.save()

        return len(chunks)
    
    def chat(self, query):
        q_emb = self.embedder.encode([query]).astype(np.float32)
        results = self.store.search(q_emb, k=3)

        retrieved_chunks = [r["meta"]["text"] for r in results]

        prompt = build_prompt(query, retrieved_chunks)

        answer = call_llm(prompt)

        return {"answer":answer, "sources":results}

