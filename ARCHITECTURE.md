# ResumeIQ Architecture

## Overview

ResumeIQ is an AI-powered resume analysis system designed to evaluate resumes through
Natural Language Processing (NLP), ATS scoring, and intelligent resume insights.

The project follows a modular architecture where each component has a single responsibility.

---

# Project Structure

```
ResumeIQ
│
├── app.py
│
├── services/
│   └── resume_analyzer.py
│
├── utils/
│   ├── parser.py
│   ├── preprocessing.py
│   ├── nlp_utils.py
│   ├── skills.py
│   ├── ats.py
│   └── section_detector.py
│
├── data/
│   └── skills.csv
│
├── templates/
├── static/
├── uploads/
└── tests/
```

---

# Resume Analysis Pipeline

```
Resume PDF
      │
      ▼
PDF Parsing
      │
      ▼
Text Preprocessing
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
ATS Engine
      │
      ▼
Frontend Report
```

---

# Module Responsibilities

## parser.py

Responsible for:

- PDF text extraction
- Handling uploaded resumes

Output

```
Raw Resume Text
```

---

## preprocessing.py

Responsible for:

- Cleaning text
- Tokenization
- Stopword removal
- Lemmatization

Output

```
Processed Tokens
```

---

## nlp_utils.py

Responsible for:

- Unigrams
- Bigrams
- Trigrams

Output

```
N-Gram Set
```

---

## skills.py

Responsible for:

- Loading skills database
- Alias resolution
- Multi-word skill detection
- Skill categorization
- Skill statistics

Output

```python
{
    "skills": {},
    "statistics": {}
}
```

---

## section_detector.py

Responsible for:

- Detecting resume sections
- Section order detection

Output

```python
{
    "summary": True,
    "education": True,
    ...
}
```

---

## ats.py

Responsible for:

- Skill Score
- Section Score
- Structure Score
- Readability Score
- Keyword Score

Output

```python
{
    "overall_score": ...,
    "breakdown": {...}
}
```

---

# ATS Scoring Model

| Component | Weight |
|-----------|--------:|
| Skills | 40 |
| Sections | 20 |
| Structure | 15 |
| Keywords | 15 |
| Readability | 10 |

Total = **100**

---

# Testing Strategy

Every major module contains dedicated unit tests.

```
tests/

test_skills.py

test_ats.py

test_section_detector.py

test_structure_score.py
```

All commits must pass the test suite before merging.

---

# Design Principles

- Modular architecture
- Single Responsibility Principle
- Configurable scoring
- Test-driven development
- Reusable utility modules
- Explainable ATS scoring

---

# Current Status

- ✅ Resume Parsing
- ✅ NLP Pipeline
- ✅ Skill Extraction
- ✅ Skill Statistics
- ✅ ATS Skill Score
- ✅ ATS Section Score
- ✅ ATS Structure Score

---

# Planned Features

- Readability Analysis
- Keyword Density Scoring
- ATS Report Generator
- Job Description Matching
- AI Resume Suggestions
- Analytics Dashboard