# 🚀 ResumeIQ – AI Resume Screening & ATS Score Predictor

<p align="center">
  <img src="<p align="center">
  <img src="https://raw.githubusercontent.com/<username>/<repository>/main/static/logo.png" width="180">
</p>" alt="ResumeIQ Logo" width="180"/>
</p>

<p align="center">
  <b>Analyze. Improve. Get Interview Ready.</b><br>
  An AI-powered resume analyzer that evaluates resumes using an ATS scoring engine,
  extracts technical skills, detects career domains, and provides personalized AI-powered
  career coaching to help candidates optimize their resumes.
</p>

---

## 📖 Overview

ResumeIQ is an intelligent resume analysis platform designed to simulate how modern Applicant Tracking Systems (ATS) evaluate resumes.

The application analyzes a candidate's resume, extracts technical skills using Natural Language Processing (NLP), calculates an ATS compatibility score, identifies missing keywords, detects suitable career domains, and generates personalized improvement suggestions using Google's Gemini AI.

Whether you're applying for internships, software engineering roles, or technical positions, ResumeIQ helps you understand exactly how your resume can be improved.

---

# ✨ Features

## 📄 Resume Parsing

- Upload resumes in PDF format
- Secure file upload using UUID-based filenames
- Automatic cleanup of uploaded files after analysis
- PDF text extraction pipeline

---

## 🧠 NLP-Based Skill Extraction

ResumeIQ performs intelligent skill extraction using:

- Text preprocessing
- Tokenization
- N-gram generation
- Alias resolution
- Multi-word skill detection
- Skill categorization

Supported categories include:

- Programming Languages
- Frameworks
- Databases
- Cloud Technologies
- DevOps Tools
- Machine Learning
- Cybersecurity
- Data Science
- Software Development
- Operating Systems

---

## 📊 ATS Score Engine

ResumeIQ evaluates resumes across multiple dimensions.

### Score Breakdown

- ✅ Skills
- ✅ Resume Sections
- ✅ Resume Structure
- ✅ Technical Profile
- ✅ Readability

The weighted scoring engine generates an overall ATS score out of **100**.

---

## 🎯 Career Domain Detection

ResumeIQ identifies the candidate's strongest career domains using a custom Technology Graph.

Examples include:

- Backend Development
- Frontend Development
- Full Stack Development
- Data Science
- Machine Learning
- Artificial Intelligence
- Cybersecurity
- Cloud Computing
- DevOps
- Mobile Development

Each detected domain includes:

- Confidence Score
- Matched Skills
- Missing Skills

---

## 💡 Missing Skills Recommendation

ResumeIQ identifies important technologies missing from your resume.

For each recommendation it provides:

- Skill Name
- Priority
- Estimated ATS Impact

Helping candidates understand what to learn next.

---

## 📈 ATS Improvement Planner

Generates personalized improvement suggestions categorized by priority.

### High Priority

Critical improvements with maximum ATS impact.

### Medium Priority

Recommended improvements.

### Low Priority

Optional enhancements.

---

## 🤖 AI Career Coach

Powered by **Google Gemini**.

Generates professional resume feedback including:

- Executive Summary
- Resume Strengths
- Areas of Improvement
- Actionable Next Steps

The AI coach explains ATS results in simple, professional language without inventing scores.

---

## 📑 Download Resume Report

Generate a professional PDF report containing:

- ATS Summary
- Score Breakdown
- Career Domains
- Detected Skills
- Missing Skills
- AI Career Coach Summary

Perfect for saving or sharing your analysis.

---

## 🎨 Modern Dashboard

Interactive results dashboard featuring:

- ATS Score Card
- Skill Categories
- Missing Keywords
- Career Domains
- AI Suggestions
- AI Career Coach
- Responsive Design

---

## 🔒 Secure File Handling

ResumeIQ follows secure upload practices.

- UUID-based filenames
- Temporary file storage
- Automatic deletion after analysis
- Secure filename sanitization

---

# 🏗️ Project Architecture

```
Resume Upload
        │
        ▼
PDF Parser
        │
        ▼
Text Preprocessing
        │
        ▼
Token Generation
        │
        ▼
N-Gram Generation
        │
        ▼
Skill Extraction
        │
        ▼
Skill Statistics
        │
        ▼
ATS Scoring Engine
        │
        ▼
Career Domain Detection
        │
        ▼
Improvement Planner
        │
        ▼
Gemini AI Career Coach
        │
        ▼
Interactive Dashboard
        │
        ▼
PDF Report Generation
```

---

# 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask

### AI

- Google Gemini API

### NLP

- Custom NLP Pipeline
- N-Gram Detection
- Skill Alias Resolution

### PDF

- ReportLab

### Testing

- Pytest

---

# 📂 Project Structure

```
ResumeIQ/
│
├── app.py
├── requirements.txt
├── README.md
│
├── services/
│   └── resume_analyzer.py
│
├── utils/
│   ├── parser.py
│   ├── preprocessing.py
│   ├── skills.py
│   ├── ats.py
│   ├── ai_coach.py
│   ├── llm_client.py
│   ├── pdf_report.py
│   └── ...
│
├── templates/
│
├── static/
│
├── uploads/
│
├── data/
│
└── tests/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ResumeIQ.git
```

Move into the project

```bash
cd ResumeIQ
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
SECRET_KEY=YOUR_SECRET_KEY
```

---

# ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 🧪 Run Tests

```bash
python -m pytest
```

---

# 🚀 Future Improvements

- Job Description Matching
- Resume Ranking
- OCR Support for Scanned PDFs
- Authentication
- Resume History
- Multiple Resume Comparison
- Recruiter Dashboard
- Cloud Deployment
- Docker Support
- Analytics Dashboard

---

# 👥 Contributors

- **Harshil Rawal**
- **Samridhi**

---

# 📜 License

This project is licensed under the MIT License.

---

<p align="center">
Built with  using Python, Flask, NLP and Google Gemini AI.
</p>