import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample skill list (can be expanded)
COMMON_SKILLS = [
    "Python", "Java", "C++", "SQL", "Machine Learning", "Data Analysis",
    "Communication", "Leadership", "Project Management", "NLP", "Deep Learning",
    "Git", "Docker", "AWS", "Cloud Computing","css","html","communication","teamwork","coordination","AI/ML"
]

def extract_skills(text):
    """Extract skills present in the text from COMMON_SKILLS list"""
    skills_found = []
    text_lower = text.lower()
    for skill in COMMON_SKILLS:
        if skill.lower() in text_lower:
            skills_found.append(skill)
    return skills_found

def compute_similarity(resume_text, job_text):
    """Compute cosine similarity between resume skills and job description skills"""
    resume_skills = " ".join(extract_skills(resume_text))
    job_skills = " ".join(extract_skills(job_text))

    vectorizer = CountVectorizer().fit_transform([resume_skills, job_skills])
    vectors = vectorizer.toarray()
    sim_score = cosine_similarity(vectors)[0][1]
    return round(sim_score * 100, 2), extract_skills(resume_text), extract_skills(job_text)

def main():
    print(" AI Resume–Job Skill Matcher")
    print("-" * 40)

    resume_text = input("Enter resume text: ")
    job_text = input("Enter job description text: ")

    match_percent, resume_skills, job_skills = compute_similarity(resume_text, job_text)
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]

    print("\n Analysis Result")
    print(f"Match Percentage : {match_percent}%")
    print(f"Resume Skills    : {', '.join(resume_skills) if resume_skills else 'None'}")
    print(f"Job Skills       : {', '.join(job_skills) if job_skills else 'None'}")
    print(f"Missing Skills   : {', '.join(missing_skills) if missing_skills else 'None'}")

    if missing_skills:
        print("\n Recommendation: Add missing skills to your resume for better match!")

if __name__ == "__main__":
    main()
