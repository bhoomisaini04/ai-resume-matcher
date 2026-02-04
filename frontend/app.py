import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("🤖 AI Resume Matcher")

tab1, tab2, tab3 = st.tabs(["Upload Resume", "Create Job", "Match & Explain"])

# -------------------------------
# Resume Upload
# -------------------------------
with tab1:
    st.header("Upload Resume")

    resume_text = st.text_area("Paste resume text")

    if st.button("Upload Resume"):
        res = requests.post(
            f"{API_URL}/resumes",
            json={"raw_text": resume_text}
        )
        if res.ok:
            st.success(f"Resume uploaded with ID: {res.json()['id']}")
        else:
            st.error(res.text)

# -------------------------------
# Job Creation
# -------------------------------
with tab2:
    st.header("Create Job")

    title = st.text_input("Job Title")
    description = st.text_area("Job Description")

    if st.button("Create Job"):
        res = requests.post(
            f"{API_URL}/jobs",
            json={"title": title, "description": description}
        )
        if res.ok:
            st.success(f"Job created with ID: {res.json()['id']}")
        else:
            st.error(res.text)

# -------------------------------
# Matching + Explanation
# -------------------------------
with tab3:
    st.header("Match Resume with Job")

    resume_id = st.number_input("Resume ID", min_value=1, step=1)
    job_id = st.number_input("Job ID", min_value=1, step=1)

    if st.button("Match"):
        res = requests.get(f"{API_URL}/match/{resume_id}/{job_id}")
        if res.ok:
            data = res.json()
            st.metric("Match Score", round(data["score"], 3))

            exp = requests.get(f"{API_URL}/explain/{resume_id}/{job_id}")
            if exp.ok:
                st.subheader("LLM Explanation")
                st.write(exp.json()["explanation"])
        else:
            st.error(res.text)
