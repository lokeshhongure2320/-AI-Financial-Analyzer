def build_prompt(context, query):
    return f"""
You are an expert financial analyst.

Use ONLY the information provided in the context below.
Do NOT make up facts. If information is missing, say "Not available in report".

---------------------
CONTEXT:
{context}
---------------------

QUESTION:
{query}

---------------------
Provide a structured answer:

1. 📊 Summary:
   - Key financial performance
   - Important highlights

2. ⚠️ Risks:
   - Business risks
   - Financial risks

3. 💡 Recommendation:
   - Investment insight (Buy / Hold / Sell)
   - Reasoning

Keep the answer clear, concise, and professional.
"""