from openai import OpenAI
import os

_client = None


def get_client():
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _client


def explain_match(job, resume_text: str, score: float) -> str:
    client = get_client()

    prompt = f"""
Job Title: {job.title}
Job Description: {job.description}

Resume:
{resume_text[:2000]}

Match Score: {score}

Explain the match briefly in simple terms.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
