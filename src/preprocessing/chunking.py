import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def chunk_text(text, max_sentences=5):
    sentences = sent_tokenize(text)

    chunks = []
    chunk = []

    for sent in sentences:
        chunk.append(sent)

        if len(chunk) >= max_sentences:
            chunks.append(" ".join(chunk))
            chunk = []

    if chunk:
        chunks.append(" ".join(chunk))

    return chunks