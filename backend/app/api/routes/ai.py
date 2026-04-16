from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import analyze_resume_with_ai

router = APIRouter()


class AIRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/ai-analysis")
def ai_analysis(data: AIRequest):
    
    result = analyze_resume_with_ai(
        data.resume_text,
        data.job_description
    )

    return {
        "analysis": result
    }