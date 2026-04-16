from fastapi import APIRouter
from pydantic import BaseModel
from app.services.job_recommender import recommend_jobs

router = APIRouter()


class JobRequest(BaseModel):
    resume_text: str


@router.post("/job-recommendation")
def get_jobs(data: JobRequest):
    return recommend_jobs(data.resume_text)