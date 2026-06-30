from utils.ats import calculate_structure_score


def test_empty_resume():
    assert calculate_structure_score("") == 0


def test_resume_with_good_structure():

    resume = """
Professional Summary

Python Developer with strong backend experience.

Education

B.Tech Mechanical Engineering

Projects

ResumeIQ

Skills

Python Flask SQL Docker Git

Experience

Backend Developer
"""

    score = calculate_structure_score(resume)

    assert score == 11