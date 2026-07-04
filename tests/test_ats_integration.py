from utils.ats import calculate_ats_score


def test_ats_response_structure():

    raw_text = """
    Professional Summary

    Python Developer

    Skills

    Python
    Flask
    SQL
    Docker
    """

    skills = {
        "Language": ["Python"],
        "Framework": ["Flask"],
        "Database": ["SQL"],
        "Tool": ["Docker"]
    }

    statistics = {
        "total_skills": 4,
        "category_distribution": {
            "Language": 1,
            "Framework": 1,
            "Database": 1,
            "Tool": 1
        }
    }

    result = calculate_ats_score(
        raw_text,
        skills,
        statistics
    )

    assert "overall_score" in result
    assert "breakdown" in result
    assert "report" in result
    assert "detected_domains" in result
    assert "improvement_plan" in result
    
def test_score_breakdown():

    raw_text = "Python Flask SQL Docker"

    skills = {
        "Language": ["Python"],
        "Framework": ["Flask"]
    }

    statistics = {
        "total_skills": 2,
        "category_distribution": {}
    }

    result = calculate_ats_score(
        raw_text,
        skills,
        statistics
    )

    breakdown = result["breakdown"]

    assert "skills" in breakdown
    assert "sections" in breakdown
    assert "structure" in breakdown
    assert "technical_profile" in breakdown
    assert "readability" in breakdown
    
def test_improvement_plan_exists():

    raw_text = "Python Flask"

    skills = {
        "Language": ["Python"],
        "Framework": ["Flask"]
    }

    statistics = {
        "total_skills": 2,
        "category_distribution": {}
    }

    result = calculate_ats_score(
        raw_text,
        skills,
        statistics
    )

    assert isinstance(
        result["improvement_plan"],
        dict
    )
    
def test_domains_are_generated():

    raw_text = """
    Python
    Flask
    SQL
    Docker
    """

    skills = {
        "Language": ["Python"],
        "Framework": ["Flask"],
        "Database": ["SQL"],
        "Tool": ["Docker"]
    }

    statistics = {
        "total_skills": 4,
        "category_distribution": {}
    }

    result = calculate_ats_score(
        raw_text,
        skills,
        statistics
    )

    assert len(result["detected_domains"]) > 0