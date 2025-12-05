# PDF RAG Bot (FastAPI + FAISS + HuggingFace + Gradio)

This project implements a Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDF documents, converts them into embeddings, performs similarity search using FAISS, and generates answers using a local HuggingFace model.  
The system includes a FastAPI backend and an optional Gradio-based user interface.

---

## Features

- Upload one or multiple PDF documents
- Extract and chunk text for efficient retrieval
- Generate embeddings using SentenceTransformers
- Store and query embeddings using FAISS
- Local LLM-based answer generation (Flan-T5-Small)
- FastAPI backend with structured endpoints
- Gradio UI for PDF upload and chat interaction
- Modular code structure for clarity and extensibility

## Technology Stack

- FastAPI (Backend API)
- FAISS (Vector store and similarity search)
- SentenceTransformers (MiniLM-L6-v2 embeddings)
- HuggingFace Transformers (Flan-T5-Small model)
- pypdf (PDF text extraction)
- Gradio (Frontend UI)
- Python 3.10+


## Project Structure
'''
pdf_ragbot/
│
├── app/
│ ├── main.py # FastAPI endpoints (upload, chat, health)
│ ├── rag.py # RAG pipeline (retrieval + generation)
│ ├── utils.py # PDF extraction and text chunking
│ ├── vector_store.py # FAISS index operations
│ ├── llm.py # Local LLM wrapper
│
├── gradio_app.py # Optional Gradio UI
├── requirements.txt
├── README.md
├── uploads/ # PDF upload directory
├── models/ # FAISS index and metadata
└── .gitignore
'''
## Installation

### 1. Clone the Repository
git clone https://github.com/Kritika-19/PDF-RAG-BOT.git
cd PDF-RAG-BOT

### 2. Create and Activate Virtual Environment
python -m venv pvenv
pvenv\Scripts\activate    # Windows

### 3. Install Dependencies
pip install -r requirements.txt

### Running the Backend (FastAPI)
Start the API server:
uvicorn app.main:app --reload
API available at:
Swagger UI: http://127.0.0.1:8000/docs
Health Check: http://127.0.0.1:8000/health

Running the Frontend (Gradio)
python gradio_app.py
Gradio will open at: http://127.0.0.1:7860

### RAG Workflow Overview
PDFs are uploaded through FastAPI or Gradio.
Text is extracted using pypdf.
Text is chunked into manageable segments.
Embeddings are created using MiniLM-L6-v2.
Embeddings are stored in a FAISS index.
User query is embedded and matched with top-k similar chunks.
Retrieved context is passed to Flan-T5-Small for answer generation.

### API Endpoints
GET /health
Health check for the backend.

POST /upload
Uploads one or more PDF files.
Content-Type: multipart/form-data
Field name: files[]

POST /chat
Accepts a query string and returns an answer along with retrieved sources.


Kritika
