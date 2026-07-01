from utils.ats import calculate_readability_score


def test_empty_resume():
    assert calculate_readability_score("") == 0


def test_good_resume():

    resume = """
Professional Summary

Experienced Backend Developer.

Skills
- Python
- Flask
- Docker
- SQL

Projects

ResumeIQ

Education

B.Tech Mechanical Engineering

Experience

Software Development Intern.
"""

    assert calculate_readability_score(resume) >= 7


def test_poor_resume():

    resume = "Python " * 40

    assert calculate_readability_score(resume) < 5