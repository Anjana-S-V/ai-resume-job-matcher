

* * * * *

AI Resume Job Matcher
=====================

AI Resume Job Matcher is a Python-based NLP application that analyzes a candidate's resume against a job description and calculates how well the candidate matches the job requirements.

The project includes:

-   A command-line implementation

-   A Streamlit-based web application

-   NLP-powered similarity scoring

-   Skill gap identification

This project demonstrates practical Natural Language Processing (NLP) and text similarity techniques in a real-world recruitment scenario.

* * * * *

 Project Overview
-------------------

Recruiters and applicants often manually compare resumes with job descriptions. This tool automates that comparison using NLP techniques.

The system:

1.  Extracts relevant skills and keywords

2.  Processes text using NLP

3.  Computes similarity score

4.  Identifies missing skills

5.  Displays a structured match analysis

The goal is to provide a simple AI-driven decision-support tool for resume optimization.

* * * * *

 Core Functionalities
-----------------------

###  Resume & Job Description Analysis

-   Accepts resume text input

-   Accepts job description text input

-   Cleans and preprocesses both texts

###  Skill Extraction

-   Extracts relevant keywords

-   Removes stopwords

-   Normalizes text for comparison

-   Uses NLP tokenization

###  Similarity Scoring

-   Uses vectorization techniques

-   Computes cosine similarity score

-   Outputs match percentage

###  Missing Skill Identification

-   Identifies keywords present in job description but missing in resume

-   Helps candidate understand skill gaps

###  Streamlit Web Interface

-   Clean and simple UI

-   Text input areas for resume and job description

-   Displays:

    -   Match percentage

    -   Extracted skills

    -   Missing skills

    -   Overall analysis

* * * * *

 Tech Stack
-------------

### Programming Language

-   Python 3.x

* * * * *

### NLP & ML Libraries

####  spaCy

-   Used for text preprocessing

-   Tokenization

-   Stopword removal

-   Linguistic normalization

####  scikit-learn

-   TF-IDF Vectorization

-   Cosine similarity scoring

-   Converts text into numerical feature vectors

* * * * *

### Web Framework

####  Streamlit

-   Builds the interactive web interface

-   Allows real-time user input

-   Displays match results dynamically

* * * * *

 How It Works (Architecture)
------------------------------

```
Resume Text Input
          ↓
Job Description Input
          ↓
Text Preprocessing (spaCy)
          ↓
TF-IDF Vectorization
          ↓
Cosine Similarity Calculation
          ↓
Match Percentage Output
          ↓
Missing Skills Identification
          ↓
Streamlit UI Display

```

* * * * *

 Project Structure
--------------------

```
Resume_analyzer/
│
├── app.py                  # Streamlit web application
├── Resume_job_matcher.py   # Core logic for text processing & scoring
├── requirements.txt        
└── README.md

```

* * * * *

 Installation & Setup
-----------------------

###  Clone the Repository

```
git clone https://github.com/Anjana-S-V/ai-resume-job-matcher.git
cd Resume_analyzer

```

* * * * *

###  Install Dependencies

```
pip install -r requirements.txt

```

If using spaCy model:

```
python -m spacy download en_core_web_sm

```

* * * * *

 Usage
--------

### Run the Streamlit Web App

```
streamlit run app.py

```

Open the browser link shown in the terminal\
(Usually: [http://localhost:8501](http://localhost:8501/))

* * * * *

 Important Notes
------------------

-   Do NOT run using:

```
python app.py

```

-   Always run with:

```
streamlit run app.py

```

-   Ensure Streamlit and spaCy model are installed before execution

* * * * *

 Output Example
-----------------

The application displays:

-   Match Percentage (e.g., 78%)

-   Extracted Resume Skills

-   Extracted Job Skills

-   Missing Skills

-   Overall Fit Assessment

* * * * *

 Privacy & Cost
-----------------

-   100% local execution

-   No cloud APIs

-   No external data storage

-   Free and open-source libraries only

* * * * *

  Learning Outcomes
--------------------

Through this project:

-   Implemented NLP preprocessing using spaCy

-   Applied TF-IDF vectorization

-   Used cosine similarity for text comparison

-   Built a real-world AI use case

-   Developed interactive web UI using Streamlit

-   Practiced modular Python project structure

* * * * *

 Future Enhancements
----------------------

-   PDF resume upload support

-   Automatic resume parsing

-   Skill weighting based on job priority

-   Resume improvement suggestions

-   Deployment via Streamlit Cloud

-   Dashboard-style analytics view

* * * * *

 Use Cases
------------

-   Students optimizing resumes

-   Job applicants tailoring resumes

-   HR screening assistance

-   NLP educational projects

-   Beginner-friendly AI demonstration

* * * * *

 Author
------------

Anjana S V\
GitHub: <https://github.com/Anjana-S-V>

