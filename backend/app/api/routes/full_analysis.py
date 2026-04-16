from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import analyze_resume_with_ai
from app.services.job_recommender import recommend_jobs

router = APIRouter()


class FullAnalysisRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/full-analysis")
def full_analysis(data: FullAnalysisRequest):

    # 🔥 Step 1: AI Analysis (ATS + skills)
    ai_result = analyze_resume_with_ai(
        data.resume_text,
        data.job_description
    )

    # 🔥 Step 2: Job Recommendation
    job_result = recommend_jobs(data.resume_text)

    # 🔥 Step 3: Combine everything
    return {
        "ats_score": ai_result.get("ats_score"),
        "missing_skills": ai_result.get("missing_skills"),
        "suggestions": ai_result.get("suggestions"),
        "recommended_roles": job_result.get("recommended_roles"),
        "career_reason": job_result.get("reason")
    }