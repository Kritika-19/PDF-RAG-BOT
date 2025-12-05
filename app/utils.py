from pypdf import PdfReader
import re

def extract_text(file_obj):
    reader = PdfReader(file_obj)
    text = ""
    for page in reader.pages:
        t = page.extract_text() or ""
        text += t + "\n"
    text  = re.sub(r"\s+", " ", text).strip()
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
        if start < 0:
            break
    return chunks
