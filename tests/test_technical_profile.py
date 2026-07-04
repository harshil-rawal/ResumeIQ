from utils.ats import calculate_technical_profile_score


def test_empty_profile():

    skills = {}

    statistics = {
        "total_skills": 0,
        "total_categories": 0
    }

    assert calculate_technical_profile_score(skills, statistics) == 0
    
def test_balanced_profile():

    skills = {
        "Language": ["Python", "Go"],
        "Framework": ["FastAPI"],
        "Cloud": ["AWS"],
        "Tool": ["Docker", "Git"],
        "Database": ["PostgreSQL"]
    }

    statistics = {
        "total_skills": 7,
        "total_categories": 5
    }

    score = calculate_technical_profile_score(
        skills,
        statistics
    )

    assert score >= 10
    
def test_single_category():

    skills = {
        "Language": [
            "Python",
            "Java",
            "C++"
        ]
    }

    statistics = {
        "total_skills": 3,
        "total_categories": 1
    }

    score = calculate_technical_profile_score(
        skills,
        statistics
    )

    assert score < 8