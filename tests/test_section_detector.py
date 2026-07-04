from utils.section_detector import detect_sections

from utils.section_detector import extract_section_positions


def test_section_positions():

    resume = """
Professional Summary

Education

Projects

Skills
"""

    positions = extract_section_positions(resume)

    assert "summary" in positions
    assert "education" in positions
    assert "projects" in positions
    assert "skills" in positions


def test_detect_sections():

    resume = """
    Professional Summary

    Education

    Projects

    Technical Skills
    """

    expected = {
        "summary": True,
        "education": True,
        "experience": False,
        "projects": True,
        "skills": True,
        "certifications": False,
        "achievements": False
    }

    assert detect_sections(resume) == expected