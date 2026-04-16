from groq import Groq
from app.core.config import GROQ_API_KEY
import json
import re

client = Groq(api_key=GROQ_API_KEY)


def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group() if match else None


def recommend_jobs(resume_text):

    prompt = f"""
    You are an AI career advisor.

    Analyze the resume and suggest best job roles.

    Return ONLY JSON:
    {{
        "recommended_roles": [list],
        "reason": "short explanation"
    }}

    Resume:
    {resume_text}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        content = response.choices[0].message.content.strip()

        json_text = extract_json(content)

        if json_text:
            return json.loads(json_text)
        else:
            return {"error": "Invalid JSON", "raw": content}

    except Exception as e:
        return {"error": str(e)}