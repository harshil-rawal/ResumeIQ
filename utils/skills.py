import pandas as pd
from pathlib import Path
from typing import Dict, List


DATA_PATH = Path(__file__).parent.parent / "data" / "skills.csv"

skill_df = pd.read_csv(DATA_PATH)

SKILL_MAP = {}
CATEGORY_MAP = {}
PRIORITY_MAP = {}
ALIAS_MAP = {}
TIER_MAP = {}

def normalize(text):
    return text.strip().lower()
for _, row in skill_df.iterrows():

    skill = normalize(row["Skill"])
    category = row["Category"]
    priority = row["Priority"]
    tier = row["Tier"].strip()

    # Store canonical skill
    SKILL_MAP[skill] = row["Skill"]
    CATEGORY_MAP[skill] = category
    PRIORITY_MAP[skill] = priority
    TIER_MAP[skill] = tier

    # Store aliases
    aliases = str(row["Aliases"]).split(";")

    for alias in aliases:

        alias = normalize(alias)

        if alias and alias != "nan":
            ALIAS_MAP[alias] = skill

def extract_skills(ngrams):
    """
    Extract skills from generated n-grams using lookup dictionaries.

    Parameters:
        ngrams (set): Set of all generated tokens, bigrams and trigrams.

    Returns:
        dict: Skills grouped by category.
    """

    extracted = {}

    # Normalize all n-grams
    normalized_tokens = {normalize(token) for token in ngrams}

    for token in normalized_tokens:

        # Resolve aliases
        if token in ALIAS_MAP:
            token = ALIAS_MAP[token]

        # Skip if not a known skill
        if token not in SKILL_MAP:
            continue

        skill_name = SKILL_MAP[token]
        category = CATEGORY_MAP[token]

        if category not in extracted:
            extracted[category] = []

        # Avoid duplicates
        if skill_name not in extracted[category]:
            extracted[category].append(skill_name)

    return extracted

def generate_skill_statistics(
    skills: Dict[str, List[str]]
) -> Dict:
    """
    Generate statistics from extracted skills.

    Parameters:
        skills (dict): Extracted skills grouped by category.

    Returns:
        dict: Summary statistics of extracted skills.
    """

    category_distribution: Dict[str, int] = {}
    total_skills = 0

    for category, skill_list in skills.items():
        count = len(skill_list)

        category_distribution[category] = count
        total_skills += count

    statistics = {
        "total_skills": total_skills,
        "total_categories": len(skills),
        "category_names": sorted(skills.keys()),
        "category_distribution": category_distribution,
        "largest_category": None,
        "smallest_category": None
    }

    if category_distribution:
        statistics["largest_category"] = max(
            category_distribution.items(),
            key=lambda item: item[1]
        )[0]

        statistics["smallest_category"] = min(
            category_distribution.items(),
            key=lambda item: item[1]
        )[0]

    return statistics

def get_skill_priority(skill):
    """
    Return the priority of a canonical skill.
    """

    skill = normalize(skill)

    return PRIORITY_MAP.get(skill, 0)

def get_skill_tier(skill):
    """
    Return the level of a skill.

    Returns:
        "Core", "Advanced", or None
    """

    normalized = normalize(skill)

    if normalized in ALIAS_MAP:
        normalized = ALIAS_MAP[normalized]
        
    
    return TIER_MAP.get(normalized)

