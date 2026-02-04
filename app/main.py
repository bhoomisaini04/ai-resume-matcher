from fastapi import FastAPI

from ai_resume_matcher.app.db import get_session
from ai_resume_matcher.app.models import Resume, Job
from ai_resume_matcher.app.matching import match_texts
from ai_resume_matcher.app.llm_explanations import explain_match
from ai_resume_matcher.app.schemas import ResumeCreate
from ai_resume_matcher.app.schemas import JobCreate

app = FastAPI(title="AI Resume Matcher")


@app.get("/health", tags=["System"])
def health():
    return {"status": "ok"}


@app.get("/explain/{resume_id}/{job_id}", tags=["LLM"])
def explain(resume_id: int, job_id: int):
    session = get_session()

    resume = session.get(Resume, resume_id)
    job = session.get(Job, job_id)

    if not resume or not job:
        return {"error": "Not found"}

    score = match_texts(resume.raw_text, job.description)
    explanation = explain_match(job, resume.raw_text, score)

    return {
        "match_score": round(score, 3),
        "explanation": explanation
    }
@app.post("/resumes")
def create_resume(payload: dict):
    session = get_session()
    resume = Resume(raw_text=payload["raw_text"])
    session.add(resume)
    session.commit()
    session.refresh(resume)
    return {"id": resume.id}

@app.post("/jobs")
def create_job(payload: dict):
    session = get_session()
    job = Job(
        title=payload["title"],
        description=payload["description"]
    )
    session.add(job)
    session.commit()
    session.refresh(job)
    return {"id": job.id}

@app.get("/match/{resume_id}/{job_id}")
def match(resume_id: int, job_id: int):
    session = get_session()
    resume = session.get(Resume, resume_id)
    job = session.get(Job, job_id)

    if not resume or not job:
        return {"error": "Not found"}

    score = match_texts(resume.raw_text, job.description)
    return {"score": score}

@app.post("/resumes")
def create_resume(payload: ResumeCreate):
    session = get_session()
    resume = Resume(raw_text=payload.raw_text)
    session.add(resume)
    session.commit()
    session.refresh(resume)
    return {"id": resume.id}

@app.post("/jobs")
def create_job(payload: JobCreate):
    session = get_session()
    job = Job(title=payload.title, description=payload.description)
    session.add(job)
    session.commit()
    session.refresh(job)
    return {"id": job.id}

@app.get("/match/{resume_id}/{job_id}")
def match(resume_id: int, job_id: int):
    session = get_session()
    resume = session.get(Resume, resume_id)
    job = session.get(Job, job_id)

    if not resume or not job:
        return {"error": "Not found"}

    score = match_texts(resume.raw_text, job.description)
    return {"score": round(score, 3)}

