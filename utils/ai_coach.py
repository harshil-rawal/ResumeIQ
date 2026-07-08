

"""
AI Career Coach for ResumeIQ
"""

SYSTEM_PROMPT = """
You are ResumeIQ AI Coach.

Your role is to explain ATS analysis in simple,
professional language.

Do not invent scores.

Only use the information provided.

Keep advice concise and actionable.

Focus on helping the candidate improve.
"""

SUMMARY = "summary"
STRENGTHS = "strengths"
IMPROVEMENTS = "improvements"
NEXT_STEPS = "next_steps"




from utils.prompt_builder import build_prompt
from utils.ai_parser import parse_ai_response
from utils.llm_client import GeminiClient


def create_empty_feedback():

    return {
        "summary": "",
        "strengths": [],
        "improvements": [],
        "next_steps": []
    }


def generate_ai_feedback(result):
    """
    Generate AI feedback using Gemini.
    """

    prompt = build_prompt(result)

    client = GeminiClient()

    response = client.generate(prompt)

    if response is None:

        feedback = {
            "summary": "AI feedback is temporarily unavailable.",
            "strengths": [],
            "improvements": [],
            "next_steps": [],
            "status": "unavailable"
        }

    else:

        feedback = parse_ai_response(response)

    return {
        "prompt": prompt,
        "feedback": feedback
    }