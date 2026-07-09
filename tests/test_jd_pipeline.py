from utils.job_description_parser import parse_job_description
from utils.jd_matcher import match_job_description


def test_complete_jd_pipeline():

    job_description = """
    Looking for a Python Developer with Flask, SQL, AWS and Git experience.
    """

    resume_skills = {
        "Language": ["Python"],
        "Framework": ["Flask"],
        "Database": ["SQL"],
        "Cloud": ["AWS"]
    }

    jd_skills = parse_job_description(job_description)

    result = match_job_description(
        resume_skills,
        jd_skills
    )

    assert result["matched_count"] == 3
    assert result["required_count"] == 4
    assert result["match_percentage"] == 75.0
    assert "Git" in result["missing_skills"]
    assert "AWS" in result["extra_skills"]