PDF RAG Bot — FastAPI + FAISS + HuggingFace + Gradio UI

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload PDFs, embeds them into a vector database using FAISS, and answers questions using a local HuggingFace LLM.
Includes both a FastAPI backend and an interactive Gradio UI.

Features
-Upload one or multiple PDF files
-Extract and chunk text from PDFs
-Generate dense embeddings using Sentence Transformers
-Store and retrieve PDF chunks using FAISS vector search
-Local LLM generation using HuggingFace FLAN-T5 (no API key needed)
-FastAPI backend with fully documented API endpoints
-Gradio UI for uploading PDFs & chatting with your bot
-Clean, modular architecture suitable for production expansion

Tech Stack
-Backend API: FastAPI
-Vector Store:	FAISS
-Embeddings:	SentenceTransformers (MiniLM-L6-v2)
-LLM: HuggingFace – Flan-T5-Small
-PDF Processing:	pypdf
-Frontend UI:	Gradio
-Environment:	Python 3.10+

Project Structure
pdf_ragbot/
│
├── app/
│   ├── main.py            # FastAPI routes (upload, chat, health)
│   ├── rag.py             # Core RAG pipeline
│   ├── utils.py           # PDF text extraction & chunking
│   ├── vector_store.py    # FAISS index handling
│   ├── llm.py             # HuggingFace model and prompting
│
├── gradio_app.py          # Gradio-based UI
├── requirements.txt
├── README.md
├── uploads/               # Uploaded PDFs (ignored in Git)
├── models/                # FAISS index & metadata (ignored in Git)
└── .gitignore

Installation
1. Clone the Repository
git clone https://github.com/Kritika-19/PDF-RAG-BOT.git
cd PDF-RAG-BOT

2️. Create & Activate Virtual Environment
python -m venv pvenv
pvenv\Scripts\activate   # Windows

3️. Install Dependencies
pip install -r requirements.txt

*Running the FastAPI Backend

Start the backend server: uvicorn app.main:app --reload

API available at:

Swagger UI → http://127.0.0.1:8000/docs

Health Check → http://127.0.0.1:8000/health

--Running the Gradio UI

In another terminal: python gradio_app.py

Gradio will open at: http://127.0.0.1:7860

* How the RAG Pipeline Works
-PDF Upload: PDF files are uploaded to FastAPI and saved locally.
-Text Extraction: pypdf extracts text from each page.
-Chunking: Text is split into overlapping chunks for better retrieval.
-Embedding: Chunks are converted into embeddings using -- all-MiniLM-L6-v2
-Vector Indexing: Embeddings are stored in a FAISS index for similarity search.
-Querying: User question → embedded → top-k chunks retrieved.
-LLM Response: Retrieved context is passed into Flan-T5-Small which generates the final answer.

*API Endpoints
GET /health:Check if the API is running.
POST /upload:Upload one or multiple PDF files.
Request:multipart/form-data with files[]
POST /chat:Ask a question.

Parameters: query: string

Response:

{
  "answer": "...",
  "sources": [...]
}

*Example Workflow

-Start FastAPI
-Open Gradio UI
-Upload your PDFs
-Ask questions like:
  "What is the document about?"
  "Summarize section 2"
  "Who is the author?"
-Model retrieves relevant chunks and answers using RAG.