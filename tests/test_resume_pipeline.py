from utils.skills import generate_skill_statistics
from utils.technology_graph import detect_domains
from utils.improvement_planner import generate_improvement_plan
from utils.ats import calculate_ats_score


def test_complete_resume_pipeline():

    raw_text = """
    Professional Summary

    Python Backend Developer

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

    statistics = generate_skill_statistics(skills)

    ats = calculate_ats_score(
        raw_text,
        skills,
        statistics
    )

    domains = detect_domains(skills)

    planner = generate_improvement_plan(
        ats["breakdown"],
        domains
    )

    assert ats["overall_score"] >= 0
    assert len(domains) > 0
    assert isinstance(planner, dict)
    
    