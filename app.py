import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Common skills list
COMMON_SKILLS = [
    "Python", "Java", "C++", "SQL", "Machine Learning", "Data Analysis",
    "Communication", "Leadership", "Project Management", "NLP",
    "Deep Learning", "Git", "Docker", "AWS", "Cloud Computing"
]

def extract_skills(text):
    skills_found = []
    text_lower = text.lower()
    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            skills_found.append(skill)
    return skills_found

def compute_match(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    resume_str = " ".join(resume_skills)
    job_str = " ".join(job_skills)

    if not resume_str or not job_str:
        return 0.0, resume_skills, job_skills, []

    vectorizer = CountVectorizer().fit_transform([resume_str, job_str])
    vectors = vectorizer.toarray()
    match_percent = cosine_similarity(vectors)[0][1] * 100

    missing_skills = [s for s in job_skills if s not in resume_skills]

    return round(match_percent, 2), resume_skills, job_skills, missing_skills


# ---------------- Streamlit UI ----------------

st.set_page_config(page_title="AI Resume Skill Matcher", page_icon="")

st.title(" AI Resume–Job Skill Matcher")
st.write("Analyze how well your resume matches a job description using AI.")

resume_text = st.text_area(" Paste your Resume Text here", height=200)
job_text = st.text_area(" Paste Job Description here", height=200)

if st.button(" Analyze Match"):
    if resume_text.strip() and job_text.strip():
        match, resume_skills, job_skills, missing_skills = compute_match(
            resume_text, job_text
        )

        st.subheader(" Match Results")
        st.metric("Match Percentage", f"{match}%")

        st.write("**Resume Skills:**", ", ".join(resume_skills) or "None")
        st.write("**Job Skills:**", ", ".join(job_skills) or "None")
        st.write("**Missing Skills:**", ", ".join(missing_skills) or "None")

        if missing_skills:
            st.info(" Tip: Add missing skills to improve your resume match.")
        else:
            st.success(" Great! Your resume matches this job well.")
    else:
        st.warning("Please enter both resume and job description.")
