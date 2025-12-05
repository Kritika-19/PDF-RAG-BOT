import faiss
import numpy as np
import os
import pickle

class FaissStore:
    def __init__(self, dim=384, index_path="models/faiss.index",meta_path="models/meta.pkl"):
        self.dim = dim
        self.index_path = index_path
        self.meta_path = meta_path
        os.makedirs("models", exist_ok=True)

        self.index = faiss.IndexFlatL2(self.dim)
        self.metadata = []

        self._load()

    def _load(self):
        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):
            try:
                self.index = faiss.read_index(self.index_path)
                with open(self.meta_path, "rb") as f:
                    self.metadata = pickle.load(f)
            except Exception as e:
                pass

    def add(self, embeddings, metas):
        self.index.add(embeddings)
        self.metadata.extend(metas)

    def search(self, query_emb, k=3):
        D, I = self.index.search(query_emb, k)
        results = []
        for dist, idx in zip(D[0], I[0]):
            results.append({
                "score": float(dist),
                "meta": self.metadata[idx]
            })
        return results
    
    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)