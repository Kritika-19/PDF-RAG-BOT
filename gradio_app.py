import gradio as gr
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

def upload_pdfs(files):
    if not files:
        return "Please upload at least one PDF file"
    
    fastapi_files = [
        ("files", ("uploaded.pdf", file, "apllication/pdf"))
        for file in files
    ]

    response = requests.post(f"{FASTAPI_URL}/upload", files=fastapi_files)

    if response.status_code != 200:
        return f"Error: {response.text}"
    
    data = response.json()
    return f"PDF uploaded successfully"

def ask_question(query):
    if not query.strip():
        return "Please enter a question"
    
    response = requests.post(f"{FASTAPI_URL}/chat", params={"query":query})

    if response.status_code != 200:
        return f"Error: {response.text}"
    
    answer = response.json().get("answer")
    return f"Answer:\n\n{answer}"

with gr.Blocks() as demo:
    gr.Markdown("# PDF RAG Bot")

    with gr.Tab("Upload PDF"):
        upload_files = gr.File(type="binary", file_count="multiple")
        upload_btn = gr.Button("Upload")
        upload_output = gr.Textbox(label="Upload Status")
        upload_btn.click(upload_pdfs, inputs=upload_files, outputs=upload_output)


    with gr.Tab("Chat with BOT"):
        query = gr.Textbox(label="Your Question")
        answer = gr.Textbox(label="Answer")
        ask_btn = gr.Button("Ask")
        ask_btn.click(ask_question, inputs=query, outputs=answer)

demo.launch()


