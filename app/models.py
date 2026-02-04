from ai_resume_matcher.app.db import engine
from typing import Optional
from sqlmodel import SQLModel, Field

class Job(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    company: str
    location: Optional[str] = None
    description: str
    requirements: Optional[str] = None
    embedding: Optional[bytes] = None

class Resume(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    candidate_name: str
    raw_text: str
    email: Optional[str] = None
    skills_extracted: Optional[str] = None
    years_experience: Optional[float] = None
    embedding: Optional[bytes] = None

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
