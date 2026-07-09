from utils.jd_matcher import match_job_description


def test_perfect_match():
    resume_skills = {
        "Programming": ["Python", "Java"],
        "Frameworks": ["Flask"]
    }

    jd_skills = {
        "Programming": ["Python", "Java"],
        "Frameworks": ["Flask"]
    }

    result = match_job_description(
        resume_skills,
        jd_skills
    )

    assert result["match_percentage"] == 100.0
    assert result["matched_count"] == 3
    assert result["required_count"] == 3
    assert result["missing_skills"] == []
    assert result["extra_skills"] == []


def test_partial_match():
    resume_skills = {
        "Programming": ["Python"],
        "Frameworks": ["Flask"]
    }

    jd_skills = {
        "Programming": ["Python"],
        "Frameworks": ["Flask", "Django"],
        "Cloud": ["AWS"]
    }

    result = match_job_description(
        resume_skills,
        jd_skills
    )

    assert result["match_percentage"] == 50.0
    assert result["matched_count"] == 2
    assert result["required_count"] == 4
    assert sorted(result["missing_skills"]) == ["AWS", "Django"]

def test_no_match():
    resume_skills = {
        "Programming": ["Java"],
        "Frameworks": ["Spring"]
    }

    jd_skills = {
        "Programming": ["Python"],
        "Frameworks": ["Flask"]
    }

    result = match_job_description(
        resume_skills,
        jd_skills
    )

    assert result["match_percentage"] == 0.0
    assert result["matched_count"] == 0
    assert result["required_count"] == 2

def test_empty_job_description():
    resume_skills = {
        "Programming": ["Python"],
        "Frameworks": ["Flask"]
    }

    jd_skills = {}

    result = match_job_description(
        resume_skills,
        jd_skills
    )

    assert result["match_percentage"] == 0.0
    assert result["required_count"] == 0        