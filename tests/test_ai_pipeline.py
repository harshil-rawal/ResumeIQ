from utils.ai_coach import generate_ai_feedback


def test_ai_pipeline():

    ats = {
        "overall_score": 82,
        "breakdown": {
            "skills": 28,
            "sections": 18,
            "structure": 13,
            "technical_profile": 15,
            "readability": 8
        },
        "report": {
            "strengths": [],
            "weaknesses": [],
            "warnings": []
        },
        "detected_domains": {},
        "improvement_plan": {}
    }

    result = generate_ai_feedback(ats)

    assert "prompt" in result
    assert "feedback" in result