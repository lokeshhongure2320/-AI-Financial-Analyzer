from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def llm(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=400   # increased for structured output
    )
    return response.choices[0].message.content


def generate(prompt):
    response = llm(prompt)

    # enforce structure
    if "Recommendation" not in response:
        return "⚠️ Output formatting failed. Try again."

    return response