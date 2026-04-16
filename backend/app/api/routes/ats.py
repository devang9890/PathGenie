from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ats_service import calculate_ats_score

router = APIRouter()


class ATSRequest(BaseModel):
    resume_text: str
    job_description: str


@router.post("/ats-score")
def get_ats_score(data: ATSRequest):
    
    result = calculate_ats_score(
        data.resume_text,
        data.job_description
    )

    return result