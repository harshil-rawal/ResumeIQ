from utils.technology_graph import detect_domains


def test_backend_has_highest_confidence():

    skills = {
        "Language": ["Python"],
        "Framework": ["Flask"],
        "Database": ["SQL"],
        "Tool": ["Docker"]
    }

    domains = detect_domains(skills)

    first = next(iter(domains))

    assert first == "Backend"
    
def test_domain_contains_score():

    skills = {
        "Language": ["Python"],
        "Framework": ["Flask"],
        "Database": ["SQL"],
        "Tool": ["Docker"]
    }

    domains = detect_domains(skills)

    backend = domains["Backend"]

    assert "domain_score" in backend
    assert "domain_max" in backend
    assert "confidence" in backend
    assert "matched_skills" in backend
    
def test_ml_detection():

    skills = {
        "Language": ["Python"],
        "Library": [
            "NumPy",
            "Pandas",
            "TensorFlow"
        ]
    }

    domains = detect_domains(skills)

    assert "Machine Learning" in domains
    
def test_missing_skills():

    skills = {
        "Language": ["Python"],
        "Framework": ["Flask"]
    }

    domains = detect_domains(skills)

    backend = domains["Backend"]

    assert "missing_skills" in backend
    assert "recommendation_score" in backend
    assert "recommendation_max" in backend
    assert "reason" in backend["missing_skills"][0]

    assert len(backend["missing_skills"]) > 0