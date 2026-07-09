from utils.job_description_parser import parse_job_description

from utils.job_description_parser import parse_job_description


def test_parse_job_description():

    job_description = """
    We are looking for a Python developer with Flask,
    Docker, Git, SQL and AWS experience.
    """

    skills = parse_job_description(job_description)

    assert "Language" in skills
    assert "Python" in skills["Language"]

    assert "Framework" in skills
    assert "Flask" in skills["Framework"]

    assert "Cloud" in skills
    assert "AWS" in skills["Cloud"]

    assert "Database" in skills
    assert "SQL" in skills["Database"]