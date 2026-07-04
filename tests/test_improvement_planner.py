from utils.improvement_planner import generate_improvement_plan


def test_generate_plan():

    scores = {
        "skills": 15,
        "sections": 10,
        "structure": 8,
        "technical_profile": 5,
        "readability": 6
    }

    plan = generate_improvement_plan(
        scores,
        {}
    )

    assert "high_priority" in plan
    assert "medium_priority" in plan
    assert "low_priority" in plan

    assert len(plan["high_priority"]) > 0
    
def test_domain_recommendation():

    scores = {
        "skills": 30,
        "sections": 18,
        "structure": 14,
        "technical_profile": 10,
        "readability": 9
    }

    detected_domains = {
    "Backend": {
        "missing_skills": [
            {
                "skill": "Kubernetes",
                "weight": 5,
                "category": "DevOps",
                "reason": "...",
                "priority": "Critical",
                "difficulty": "Advanced",
                "estimated_learning_time": "4-8 weeks"
            },
            {
                "skill": "Redis",
                "weight": 4,
                "category": "Database",
                "reason": "...",
                "priority": "High",
                "difficulty": "Intermediate",
                "estimated_learning_time": "2-4 weeks"
            },
            {
                "skill": "AWS",
                "weight": 3,
                "category": "Cloud",
                "reason": "...",
                "priority": "Medium",
                "difficulty": "Intermediate",
                "estimated_learning_time": "2-4 weeks"
            }
        ]
    }
}

    plan = generate_improvement_plan(
        scores,
        detected_domains
    )
    
    backend = plan["high_priority"][0]

    assert len(backend["actions"]) == 3

    assert backend["actions"][0]["skill"] == "Kubernetes"
    assert backend["actions"][0]["category"] == "DevOps"
    assert "reason" in backend["actions"][0]
    assert "weight" in backend["actions"][0]
    assert "priority" in backend["actions"][0]
    assert "difficulty" in backend["actions"][0]
    assert "estimated_learning_time" in backend["actions"][0]

    assert len(plan["high_priority"]) > 0