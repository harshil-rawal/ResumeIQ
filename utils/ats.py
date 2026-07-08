from utils.skills import (
    get_skill_priority,
    get_skill_tier
)
from utils.section_detector import (
    detect_sections,
    extract_section_positions
)

from utils.technology_graph import detect_domains
from utils.improvement_planner import generate_improvement_plan
from utils.report_generator import generate_report

"""
ATS Scoring Engine for ResumeIQ
"""

ATS_WEIGHTS = {
    "skills": 40,
    "sections": 20,
    "structure": 15,
    "technical_profile": 15,
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

READABILITY_CONFIG = {
    "ideal_word_range": (200, 700),
    "acceptable_word_range": (100, 1000),
    "ideal_sentence_range": (10, 25),
    "minimum_paragraphs": 10,
    "minimum_bullets": 4
}

ATS_STRUCTURE_CONFIG = {
    "ideal_word_count": (300, 800),
    "acceptable_word_count": (150, 1000),
    "ideal_sections": 5,
    "minimum_sections": 3,
    "ideal_paragraphs": 4,
    "minimum_paragraphs": 2
}

TECHNICAL_PROFILE_CONFIG = {
    "coverage": [
        (15, 5),
        (10, 4),
        (5, 3),
        (1, 2),
        (0, 0)
    ],

    "diversity": [
        (5, 4),
        (4, 3),
        (3, 2),
        (2, 1),
        (0, 0)
    ],

    "advanced": [
        (6, 3),
        (4, 2),
        (2, 1),
        (0, 0)
    ],

    "balance": [
        (5, 3),
        (3, 2),
        (2, 1),
        (0, 0)
    ]
}

TECH_ECOSYSTEMS = {
    "Backend": {
        "Python",
        "Flask",
        "FastAPI",
        "SQL",
        "Docker",
        "Git"
    },

    "AI": {
        "Python",
        "NumPy",
        "Pandas",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch"
    },

    "Cloud": {
        "AWS",
        "Docker",
        "Kubernetes",
        "Linux"
    },

    "Frontend": {
        "JavaScript",
        "TypeScript",
        "React",
        "Angular",
        "Vue"
    }
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

    return min(score, ATS_WEIGHTS["structure"])

import re

def calculate_readability_score(raw_text):
    """
    Calculate readability score out of 10.
    """

    text = raw_text.strip()

    if not text:
        return 0

    score = 0

    # -------------------------
    # Word Count
    # -------------------------
    words = text.split()
    word_count = len(words)

    ideal_min, ideal_max = READABILITY_CONFIG["ideal_word_range"]
    acceptable_min, acceptable_max = READABILITY_CONFIG["acceptable_word_range"]

    if ideal_min <= word_count <= ideal_max:
        score += 3
    elif acceptable_min <= word_count <= acceptable_max:
        score += 2
    elif word_count > 0:
        score += 1

    # -------------------------
    # Sentence Length
    # -------------------------
    sentences = re.split(r"[.!?]+", text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if sentences:
        average_length = word_count / len(sentences)

        min_len, max_len = READABILITY_CONFIG["ideal_sentence_range"]

        if min_len <= average_length <= max_len:
            score += 3
        elif average_length > 0:
            score += 2

    # -------------------------
    # Organization
    # -------------------------
    non_empty_lines = [
        line for line in text.splitlines()
        if line.strip()
    ]

    if len(non_empty_lines) >= READABILITY_CONFIG["minimum_paragraphs"]:
        score += 2
    elif len(non_empty_lines) >= 5:
        score += 1

    # -------------------------
    # Bullet Points
    # -------------------------
    bullet_count = 0

    for line in non_empty_lines:
        if line.strip().startswith(("-", "*", "•")):
            bullet_count += 1

    if bullet_count >= READABILITY_CONFIG["minimum_bullets"]:
        score += 2
    elif bullet_count >= 2:
        score += 1
    
    
    return min(score, ATS_WEIGHTS["readability"])

def calculate_ats_score(raw_text, skills, statistics):
    """
    Calculate the complete ATS score.
    """

    scores = {
        "skills": calculate_skill_score(skills, statistics),
        "sections": calculate_section_score(raw_text),
        "structure": calculate_structure_score(raw_text),
        "technical_profile": calculate_technical_profile_score(
            skills,
            statistics
        ),
        "readability": calculate_readability_score(raw_text)
    }

    overall_score = min(sum(scores.values()),100)
    report = generate_report(scores)

    detected_domains = detect_domains(skills)
    improvement_plan = generate_improvement_plan(
        scores,
        detected_domains
    )


    return {
        "overall_score": overall_score,
        
        "scores": scores,

        "breakdown": {
            "skills": {
                "score": scores["skills"],
                "max": ATS_WEIGHTS["skills"]
            },

            "sections": {
                "score": scores["sections"],
                "max": ATS_WEIGHTS["sections"]
            },

            "structure": {
                "score": scores["structure"],
                "max": ATS_WEIGHTS["structure"]
            },

           "technical_profile": {
                "score": scores["technical_profile"],
                "max": ATS_WEIGHTS["technical_profile"]
            },

            "readability": {
                "score": scores["readability"],
                "max": ATS_WEIGHTS["readability"]
            }
        },
        
        "report": report,
        
        "detected_domains": detected_domains,
        "improvement_plan": improvement_plan
    }
    
def score_from_threshold(value, thresholds):
    """
    Return score based on threshold table.
    """

    for minimum, score in thresholds:
        if value >= minimum:
            return score

    return 0

def calculate_technical_profile_score(skills, statistics):
    """
    Calculate the technical profile score out of 15.
    """

    score = 0

    total_skills = statistics.get("total_skills", 0)
    total_categories = statistics.get("total_categories", 0)

    score += score_from_threshold(
        total_skills,
        TECHNICAL_PROFILE_CONFIG["coverage"]
    )

    score += score_from_threshold(
        total_categories,
        TECHNICAL_PROFILE_CONFIG["diversity"]
    )

    advanced_count = 0

    for category in skills.values():

        for skill in category:

            if get_skill_tier(skill) == "Advanced":
                advanced_count += 1

    score += score_from_threshold(
        advanced_count,
        TECHNICAL_PROFILE_CONFIG["advanced"]
    )

    score += score_from_threshold(
        total_categories,
        TECHNICAL_PROFILE_CONFIG["balance"]
    )

    return min(score, ATS_WEIGHTS["technical_profile"])