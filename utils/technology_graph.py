import json
from pathlib import Path

GRAPH_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "technology_graph.json"
)

with open(GRAPH_PATH, encoding="utf-8") as file:
    TECHNOLOGY_GRAPH = json.load(file)
    
def flatten_skills(skills):
    """
    Convert categorized skills into a single set.
    """

    return {
        skill.lower().strip()
        for category in skills.values()
        for skill in category
    }
    
def detect_domains(skills):
    """
    Detect technology domains from extracted skills.

    Parameters:
        skills (dict): Skills grouped by category.

    Returns:
        dict: Detected domains with confidence scores.
    """

    resume_skills = flatten_skills(skills)

    detected = {}

    for domain, data in TECHNOLOGY_GRAPH.items():

        domain_score = 0
        domain_max = 0

        recommendation_score = 0
        recommendation_max = 0

        matched = []
        missing = []

        # -------------------------
        # Domain Detection
        # (Required + Frameworks)
        # -------------------------

        for section_name in ["required", "frameworks"]:

            section = data[section_name]

            for skill, details in section.items():

                weight = details["weight"]

                domain_max += weight
                resume_skills = {
                    skill.lower().strip()
                    for skill in flatten_skills(skills)
                }
                if skill.lower() in resume_skills:

                    domain_score += weight
                    matched.append(skill)
                    
        # -------------------------
        # Recommendation Analysis
        # (Recommended + Advanced)
        # -------------------------

        for section_name in ["recommended", "advanced"]:

            section = data[section_name]

            for skill, details in section.items():

                weight = details["weight"]

                recommendation_max += weight

                if skill.lower() in resume_skills:

                    recommendation_score += weight

                else:

                    missing.append(
                        {
                            "skill": skill,
                            "weight": weight,
                            "category": details["category"],
                            "reason": details["reason"],
                            "priority": details["priority"],
                            "difficulty": details["difficulty"],
                            "estimated_learning_time": details["estimated_learning_time"]
                        }
                    )

        confidence = round(
            domain_score / domain_max,
            2
        ) if domain_max else 0

        # Ignore very weak matches
        if confidence >= 0.10:

            detected[domain] = {
                "confidence": confidence,
                "matched_skills": sorted(matched),
                
                "missing_skills": sorted(
                    missing,
                    key=lambda skill: skill["weight"],
                    reverse=True
                ),
                "domain_score": domain_score,
                "domain_max": domain_max,
                "recommendation_score": recommendation_score,
                "recommendation_max": recommendation_max
            }

    # Sort by confidence (highest first)
    detected = dict(
        sorted(
            detected.items(),
            key=lambda item: item[1]["confidence"],
            reverse=True
        )
    )
    print(resume_skills)
    print(detected)

    return detected