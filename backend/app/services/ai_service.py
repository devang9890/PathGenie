import re
import json
from groq import Groq
from app.core.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def extract_json(text):
    # Extract JSON block using regex
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group()
    return None


def analyze_resume_with_ai(resume_text, job_description):

    prompt = f"""
    You are an AI career assistant.

    Analyze the resume and job description.

    STRICTLY return ONLY valid JSON:
    {{
        "ats_score": number,
        "missing_skills": [list],
        "suggestions": [list]
    }}

    Do NOT add any explanation.

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        content = response.choices[0].message.content.strip()

        # 🔥 Extract JSON safely
        json_text = extract_json(content)

        if json_text:
            data = json.loads(json_text)
            
            # convert to %
            if "ats_score" in data:
                data["ats_score"] = round(data["ats_score"] * 100, 2)
            
            return data
        else:
            return {"error": "Invalid JSON format", "raw": content}

    except Exception as e:
        return {"error": str(e)}