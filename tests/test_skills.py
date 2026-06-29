from utils.skills import extract_skills

text = """
python flask sql docker git numpy pandas tensorflow
"""

skills = extract_skills(text)

print(skills)