import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = re.sub(r'([a-z])\s([a-z])', r'\1\2', text)  # fix broken words
    return text.strip()