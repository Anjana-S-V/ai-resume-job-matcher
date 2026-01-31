# AI Resume Job Matcher

AI Resume Job Matcher is a Python-based application that compares a resume with a job description and calculates how well the candidate's skills match the job requirements. The project includes both a command-line version and a Streamlit web application for easier interaction.

---

## Features

- Extracts skills from resume and job description text
- Calculates match percentage using similarity scoring
- Identifies missing skills
- Web-based interface using Streamlit
- Simple and beginner-friendly AI project

---

## Technologies Used

- Python 3
- Streamlit
- spaCy
- scikit-learn

---

## Installation

1. Clone the repository:

git clone https://github.com/Anjana-S-V/ai-resume-job-matcher.git


2. Navigate to the project folder:

cd Resume_analyzer


3. Install dependencies:

pip install -r requirements.txt


---

## Usage

### Run the Streamlit Web App

streamlit run app.py


Open the browser link shown in the terminal (usually http://localhost:8501).

---

## Project Structure

Resume_analyzer
- app.py
- Resume_job_matcher.py
- requirements.txt
- README.md


---

## Notes

- Do not run `app.py` using `python app.py`
- Always use `streamlit run app.py` to avoid runtime warnings
- Ensure Streamlit is installed before running the app

---

## Future Enhancements

- Resume PDF upload support
- Skill weighting based on job importance
- Online deployment using Streamlit Cloud
- Resume improvement suggestions

---

## Author

Anjana S V  
GitHub: https://github.com/Anjana-S-V
