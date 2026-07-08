from utils.prompt_builder import (
    format_overall_score,
    format_breakdown,
    build_prompt
)


def test_overall_score():

    result = {
        "overall_score": 87
    }

    text = format_overall_score(result)

    assert "87" in text


def test_prompt_contains_score():

    result = {
        "overall_score": 87,
        "breakdown": {},
        "report": {},
        "detected_domains": {},
        "improvement_plan": {}
    }

    prompt = build_prompt(result)

    assert "87" in prompt
    assert "ResumeIQ AI Coach" in prompt