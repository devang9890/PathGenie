from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from app.services.skill_gap import analyze_skill_gap

router = APIRouter()


class SkillGapRequest(BaseModel):
    missing_keywords: List[str]


@router.post("/skill-gap")
def get_skill_gap(data: SkillGapRequest):
    
    suggestions = analyze_skill_gap(data.missing_keywords)

    return {
        "suggestions": suggestions
    }