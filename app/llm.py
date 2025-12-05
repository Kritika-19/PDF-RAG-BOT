from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load a small local model
MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def build_prompt(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)
    prompt = f"""
    Context:
    {context}

    Question: {query}
    Answer:
    """
    return prompt

def call_llm(prompt, max_tokens=128):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=max_tokens,
        num_beams=2,
        early_stopping=True
    )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer
