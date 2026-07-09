"""
Prompt Builder for ResumeIQ AI Coach
"""

SUMMARY = "summary"
STRENGTHS = "strengths"
WEAKNESSES = "weaknesses"
WARNINGS = "warnings"

HIGH = "high_priority"
MEDIUM = "medium_priority"
LOW = "low_priority"

def format_overall_score(result):
    return (
        "Overall ATS Score:\n"
        f"{result['overall_score']}/100\n"
    )
    
def format_breakdown(result):

    breakdown = result["breakdown"]

    lines = [
        "\nScore Breakdown",
        "---------------"
    ]

    for metric, score in breakdown.items():

        lines.append(
            f"{metric.replace('_',' ').title()}: {score}"
        )

    return "\n".join(lines)

def format_report(result):

    report = result["report"]

    lines = [
        "\nReport",
        "------"
    ]

    for section in [
        STRENGTHS,
        WEAKNESSES,
        WARNINGS
    ]:

        lines.append(
            f"\n{section.title()}"
        )

        for item in report.get(section, []):

            lines.append(
                f"- {item['message']}"
            )

    return "\n".join(lines)

def format_domains(result):

    domains = result["detected_domains"]

    lines = [
        "\nDetected Domains",
        "----------------"
    ]

    for domain, details in domains.items():

        lines.append(
            f"{domain}: {details['confidence']:.2f}"
        )

    return "\n".join(lines)

def format_planner(result):

    planner = result["improvement_plan"]

    lines = [
        "\nImprovement Plan",
        "----------------"
    ]

    for priority, suggestions in planner.items():

        lines.append(
            f"\n{priority.replace('_',' ').title()}"
        )

        for suggestion in suggestions:

            lines.append(
                f"- {suggestion['title']}"
            )

    return "\n".join(lines)

def build_prompt(result):

    prompt = [
        "You are ResumeIQ AI Coach.",
        "",
        "Analyze the ATS report.",
        "",
        format_overall_score(result),
        format_breakdown(result),
        format_report(result),
        format_domains(result),
        format_planner(result),
        "",
        

        (
            "Base your recommendations primarily on:\n"
            "1. High Priority improvement plan.\n"
            "2. Detected technical domains.\n"
            "3. ATS weaknesses.\n"
            "4. ATS warnings.\n\n"
        ),

        (
            "Respond ONLY with valid JSON.\n"
            "Do NOT include markdown.\n"
            "Do NOT include code fences.\n"
            "Do NOT explain the JSON.\n\n"

            "Writing Rules:\n"

            "- Write concise dashboard-friendly content.\n"
            "- Avoid repeating the same advice.\n"
            "- Mention technologies only if supported by the ATS analysis.\n"
            "- Use professional and encouraging language.\n"
            "- Personalize the advice using the detected domains.\n"
            "- Mention backend, frontend, AI, cloud, or data science only when detected.\n"
            "- Never recommend technologies unrelated to the detected profile.\n"
            "- Do not invent scores or skills.\n\n"

            "Summary Rules:\n"

            "- Maximum 40 words.\n"
            "- Mention one major strength and one major improvement area.\n"
            "- Write as one short paragraph.\n\n"

            "Strength Rules:\n"

            "- Exactly 4 strengths.\n"
            "- Maximum 10 words each.\n"
            "- No explanations.\n"
            "- No repeated ideas.\n\n"

            "Improvement Rules:\n"

            "- Exactly 4 improvements.\n"
            "- Begin each item with an action verb.\n"
            "- Maximum 12 words each.\n"
            "- Be specific.\n\n"

            "Next Step Rules:\n"

            "- Exactly 4 next steps.\n"
            "- Maximum 15 words each.\n"
            "- Order from highest priority to lowest.\n"
            "- Each step should be actionable.\n\n"

            "Return EXACTLY this JSON:\n\n"

            "{\n"
            '  "summary": "",\n'
            '  "strengths": [],\n'
            '  "improvements": [],\n'
            '  "next_steps": []\n'
            "}"
        )
    ]

    return "\n".join(prompt)