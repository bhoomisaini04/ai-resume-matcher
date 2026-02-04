from sklearn.metrics.pairwise import cosine_similarity
from ai_resume_matcher.app.embeddings import embed
import numpy as np

def match_texts(resume_text: str, job_text: str) -> float:
    r_emb = embed(resume_text)
    j_emb = embed(job_text)
    return float(cosine_similarity([r_emb], [j_emb])[0][0])
