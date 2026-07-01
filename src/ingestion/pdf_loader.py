import os
import pdfplumber

def load_pdfs(path):
    text = ""

    #   CASE 1: single PDF file
    if path.endswith(".pdf"):
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        return [text]

    #  CASE 2: folder
    texts = []

    for file in os.listdir(path):
        if file.endswith(".pdf"):
            file_path = os.path.join(path, file)

            with pdfplumber.open(file_path) as pdf:
                temp = ""
                for page in pdf.pages:
                    temp += page.extract_text() or ""

            texts.append(temp)

    return texts