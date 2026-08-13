import json
import os

from src.vectorstore.embedder import model, embed
from src.vectorstore.faiss_db import create_index
from src.retrieval.retriever import search

from src.analytics.sentiment import sentiment_score
from src.analytics.stock_analysis import stock_summary

from src.llm.model import generate
from src.llm.prompt_template import build_prompt


CHUNKS_PATH = "data/processed/chunks.json"

def load_chunks():
    if not os.path.exists(CHUNKS_PATH):
        raise FileNotFoundError("chunks.json not found. Run data_pipeline first.")

    with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

chunks = load_chunks()
embeddings = embed(chunks)
index = create_index(embeddings)


def run_pipeline(query):
    chunks = load_chunks()

    # Step 1: Embed all chunks
    embeddings = embed(chunks)

    # Step 2: Create FAISS index
    index = create_index(embeddings)

    # Step 3: Retrieve relevant chunks
    top_chunks = search(query, model, index, chunks, k=5)

    # Step 4: Build context
    context = "\n".join(top_chunks)

    # Step 5: Build prompt
    prompt = build_prompt(query, context)

    response = generate(prompt)
    return response