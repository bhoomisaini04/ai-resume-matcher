from ai_resume_matcher.app.models import Resume
from typing import Optional
from pydantic import BaseModel

class JobCreate(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    description: str
    requirements: Optional[str] = None

class JobRead(BaseModel):
    id: int
    title: str
    company: str
    location: Optional[str] = None

class ResumeCreate(BaseModel):
    candidate_name: str
    raw_text: str

class ResumeRead(BaseModel):
    id: int
    candidate_name: str
    email: Optional[str] = None
    skills_extracted: Optional[str] = None
    years_experience: Optional[float] = None

class MatchResult(BaseModel):
    job_id: int
    job_title: str
    score: float
    explanation: Optional[str] = None
