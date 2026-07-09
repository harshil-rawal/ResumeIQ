"""
Job Description Matching Module
"""


def match_job_description(resume_skills, jd_skills):
    """
    Compare resume skills with job description skills.

    Args:
        resume_skills (dict): Skills extracted from the resume.
        jd_skills (dict): Skills extracted from the job description.

    Returns:
        dict: JD matching results.
    """

    # Convert resume skills into a single set
    resume_set = set()

    for skill_list in resume_skills.values():
        resume_set.update(skill_list)

    # Convert JD skills into a single set
    jd_set = set()

    for skill_list in jd_skills.values():
        jd_set.update(skill_list)

    matched_skills = sorted(resume_set & jd_set)

    missing_skills = sorted(jd_set - resume_set)

    extra_skills = sorted(resume_set - jd_set)    

    matched_count = len(matched_skills)
    required_count = len(jd_set)

    if required_count == 0:
        match_percentage = 0.0
    else:
        match_percentage = round(
            (matched_count / required_count) * 100,
            2
        )

    return {
    "match_percentage": match_percentage,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "extra_skills": extra_skills,
    "matched_count": matched_count,
    "required_count": required_count
}    