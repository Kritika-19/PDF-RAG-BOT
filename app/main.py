from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from .rag import RAGBot

app = FastAPI()
rag = RAGBot()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    total_chunks = 0

    for file in files:
        file_path = f"{UPLOAD_DIR}/{file.filename}"

        
        filepath = f"{UPLOAD_DIR}/{file.filename}"
        with open(filepath, "wb") as f:
            shutil.copyfileobj(file.file, f)

        chunks_added = rag.index_pdf(filepath, source=file.filename)
        total_chunks += chunks_added

    return {"status": "indexed", "chunks": total_chunks}

@app.post("/chat")
async def chat(query: str):
    return rag.chat(query)