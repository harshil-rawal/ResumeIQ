from utils.ai_coach import (
    build_prompt,
    generate_ai_feedback
)


def test_prompt_generation():

    ats = {
        "overall_score": 85,
        "breakdown": {},
        "report": {},
        "detected_domains": {},
        "improvement_plan": {}
    }

    prompt = build_prompt(ats)

    assert "85" in prompt
    assert "ResumeIQ AI Coach" in prompt
    assert "Overall ATS Score" in prompt


def test_feedback_structure():

    ats = {
        "overall_score": 85,
        "breakdown": {},
        "report": {},
        "detected_domains": {},
        "improvement_plan": {}
    }

    feedback = generate_ai_feedback(ats)

    assert "prompt" in feedback
    assert "feedback" in feedback

    assert "summary" in feedback["feedback"]
    assert "strengths" in feedback["feedback"]
    assert "improvements" in feedback["feedback"]
    assert "next_steps" in feedback["feedback"]