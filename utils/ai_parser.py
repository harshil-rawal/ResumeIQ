import json
import re


def parse_ai_response(response):
    """
    Parse Gemini response into Python dictionary.
    """

    # Remove markdown code fences
    response = re.sub(
        r"```json|```",
        "",
        response
    ).strip()

    try:
        return json.loads(response)

    except json.JSONDecodeError:

        return {
            "summary": "Unable to parse AI response.",
            "strengths": [],
            "improvements": [],
            "next_steps": []
        }