A Streamlit-based ATS-inspired Resume Analyzer that compares uploaded resumes with job descriptions to evaluate skill compatibility and overall job fit. The application extracts text from PDF resumes, cleans and processes the content using NLP techniques, identifies matching and missing skills, calculates a resume match percentage, and provides experience-level feedback based on job requirements.

Features:
- Upload and analyze PDF resumes
- Match resume skills with job description skills
- Detect matched and missing skills
- Calculate resume match percentage
- Experience fit assessment
- Interactive Streamlit UI
- 
Technologies Used
- Python
- Streamlit
- pdfplumber

Live Demo:
https://resume-analyzer-job-matcher.streamlit.app/

Run Locally:
pip install -r requirements.txt
streamlit run app.py
