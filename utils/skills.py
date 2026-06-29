import pandas as pd

skills_df = pd.read_csv("data/skills.csv")

skill_dict = {}

for _, row in skills_df.iterrows():

    skill_dict[row["Skill"].lower()] = {
        "name": row["Skill"],
        "category": row["Category"]
    }


def extract_skills(ngrams):
    """
    Extract skills from preprocessed resume text.
    """

    tokens = ngrams

    extracted = {}

    for skill, info in skill_dict.items():

        if skill in tokens:

            category = info["category"]
            name = info["name"]

            if category not in extracted:
                extracted[category] = []

            extracted[category].append(name)

    return extracted