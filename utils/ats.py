from utils.skills import get_skill_priority
from utils.section_detector import (
    detect_sections,
    extract_section_positions
)

"""
ATS Scoring Engine for ResumeIQ
"""

ATS_WEIGHTS = {
    "skills": 40,
    "sections": 20,
    "structure": 15,
    "keywords": 15,
    "readability": 10
}

SKILL_SCORE_THRESHOLDS = {
    "total_skills": [
        (15, 15),
        (10, 11),
        (5, 7),
        (1, 3),
        (0, 0)
    ],

    "categories": [
        (5, 10),
        (4, 8),
        (3, 6),
        (2, 4),
        (1, 2),
        (0, 0)
    ],

    "priority_skills": [
        (9, 10),
        (6, 8),
        (3, 5),
        (1, 2),
        (0, 0)
    ]
}

ATS_STRUCTURE_CONFIG = {
    "ideal_word_count": (300, 800),
    "acceptable_word_count": (150, 1000),
    "ideal_sections": 5,
    "minimum_sections": 3,
    "ideal_paragraphs": 4,
    "minimum_paragraphs": 2
}


def calculate_skill_score(skills, statistics):
    """
    Calculate ATS skill score out of 40.
    """
    if statistics.get("total_skills", 0) == 0:
        return 0
    
    score = 0

    total_skills = statistics.get("total_skills", 0)
    total_categories = statistics.get("total_categories", 0)
    
    # -----------------------------
    # Total Skills Score (15)
    # -----------------------------
    for threshold, points in SKILL_SCORE_THRESHOLDS["total_skills"]:
        if total_skills >= threshold:
            score += points
            break

    # -----------------------------
    # Category Diversity Score (10)
    # -----------------------------
    for threshold, points in SKILL_SCORE_THRESHOLDS["categories"]:
        if total_categories >= threshold:
            score += points
            break

    # -----------------------------
    # Priority Skill Score (10)
    # -----------------------------
    priority_count = 0

    for category in skills.values():
        for skill in category:
            if get_skill_priority(skill) == 1:
                priority_count += 1

    for threshold, points in SKILL_SCORE_THRESHOLDS["priority_skills"]:
        if priority_count >= threshold:
            score += points
            break

    # -----------------------------
    # Balanced Profile Score (5)
    # -----------------------------
    if total_categories >= 5:
        score += 5
    elif total_categories >= 3:
        score += 3
    elif total_categories >= 2:
        score += 2
    elif total_categories >= 1:
        score += 1

    return min(score, ATS_WEIGHTS["skills"])

def calculate_section_score(raw_text):
    """
    Calculate ATS score based on resume sections.
    """

    sections = detect_sections(raw_text)

    score = 0

    if sections["summary"]:
        score += 2

    if sections["education"]:
        score += 4

    if sections["experience"]:
        score += 5

    if sections["projects"]:
        score += 4

    if sections["skills"]:
        score += 3

    if sections["certifications"]:
        score += 1

    if sections["achievements"]:
        score += 1

    return min(score, ATS_WEIGHTS["sections"])


def calculate_structure_score(raw_text):
    """
    Evaluate the structural quality of the resume.
    """

    score = 0

    text = raw_text.strip()

    if not text:
        return 0

    # -------------------------
    # Resume is not empty
    # -------------------------
    score += 3

    # -------------------------
    # Word Count
    # -------------------------
    word_count = len(text.split())

    ideal_min, ideal_max = ATS_STRUCTURE_CONFIG["ideal_word_count"]
    acceptable_min, acceptable_max = ATS_STRUCTURE_CONFIG["acceptable_word_count"]

    if ideal_min <= word_count <= ideal_max:
        score += 4
    elif acceptable_min <= word_count <= acceptable_max:
        score += 2

    # -------------------------
    # Section Coverage
    # -------------------------
    sections = detect_sections(raw_text)

    section_count = sum(sections.values())

    if section_count >= ATS_STRUCTURE_CONFIG["ideal_sections"]:
        score += 5
    elif section_count >= ATS_STRUCTURE_CONFIG["minimum_sections"]:
        score += 3
    elif section_count >= 1:
        score += 1
        
    # -------------------------
    # Section Order
    # -------------------------

    positions = extract_section_positions(raw_text)

    ordered = list(positions.values()) == sorted(positions.values())

    if ordered and len(positions) >= 4:
        score += 3
    elif len(positions) >= 2:
        score += 2
        
    print(sections)
    print(positions)


    return min(score, ATS_WEIGHTS["structure"])


def calculate_keyword_score(skills):
    """
    Evaluate keyword coverage and distribution.
    """
    return 0


def calculate_readability_score(raw_text):
    """
    Evaluate readability of the resume.
    """
    return 0

def calculate_ats_score(raw_text, skills, statistics):
    """
    Calculate the complete ATS score.
    """

    scores = {
        "skills": calculate_skill_score(skills, statistics),
        "sections": calculate_section_score(raw_text),
        "structure": calculate_structure_score(raw_text),
        "keywords": calculate_keyword_score(skills),
        "readability": calculate_readability_score(raw_text)
    }

    overall_score = sum(scores.values())

    return {
        "overall_score": overall_score,
        "breakdown": scores
    }