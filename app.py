import streamlit as st
from src.pipeline.rag_pipeline import run_pipeline

st.title("📊 AI Financial Analyzer")

query = st.text_input("Ask your question")

if query:
    result = run_pipeline(query)
    st.write(result)