import json
import os

from src.ingestion.pdf_loader import load_pdfs
from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.chunking import chunk_text


def process_data():
    print("Pipeline started")

    texts = load_pdfs("data/raw/pdf_reports.pdf")

    all_chunks = []

    for text in texts:
        clean = clean_text(text)
        chunks = chunk_text(clean)
        all_chunks.extend(chunks)

    print("Total chunks:", len(all_chunks))

    #  Ensure folder exists
    os.makedirs("data/processed", exist_ok=True)

    #  Write file
    file_path = "data/processed/chunks.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    print("chunks.json CREATED at:", file_path)


if __name__ == "__main__":
    process_data()