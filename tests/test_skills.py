from utils.skills import extract_skills
from utils.skills import generate_skill_statistics


def test_basic_skills():
    ngrams = {
        "python",
        "flask",
        "sql",
        "git"
    }

    expected = {
        "Language": ["Python"],
        "Framework": ["Flask"],
        "Database": ["SQL"],
        "Tool": ["Git"]
    }

    assert extract_skills(ngrams) == expected


def test_aliases():
    ngrams = {
        "js",
        "cpp",
        "ml"
    }

    expected = {
        "Language": ["JavaScript", "C++"],
        "Concept": ["Machine Learning"]
    }

    result = extract_skills(ngrams)

    assert set(result["Language"]) == {"JavaScript", "C++"}
    assert set(result["Concept"]) == {"Machine Learning"}


def test_multiword_skills():
    ngrams = {
        "machine learning",
        "deep learning",
        "natural language processing"
    }

    expected = {
        "Concept": [
            "Machine Learning",
            "Deep Learning",
            "Natural Language Processing"
        ]
    }

    result = extract_skills(ngrams)

    assert set(result["Concept"]) == {
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing"
    }


def test_duplicate_skills():
    ngrams = {
        "python",
        "py",
        "PYTHON"
    }

    expected = {
        "Language": ["Python"]
    }

    assert extract_skills(ngrams) == expected


def test_unknown_skills():
    ngrams = {
        "resumeiq",
        "pizza",
        "chatgpt"
    }

    result = extract_skills(ngrams)

def test_skill_statistics():

    skills = {
        "Language": ["Python", "Java"],
        "Framework": ["Flask"],
        "Tool": ["Git", "Docker"]
    }

    expected = {
        "total_skills": 5,
        "total_categories": 3,
        "category_names": [
            "Framework",
            "Language",
            "Tool"
        ],
        "category_distribution": {
            "Language": 2,
            "Framework": 1,
            "Tool": 2
        },
        "largest_category": "Language",
        "smallest_category": "Framework"
    }

    assert generate_skill_statistics(skills) == expected 