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
            "Respond ONLY with valid JSON.\n"
            "Do not include markdown.\n"
            "Do not include code fences.\n"
            "Do not include any explanation.\n\n"
            "Return exactly this structure:\n\n"
            "{\n"
            '  "summary": "",\n'
            '  "strengths": [],\n'
            '  "improvements": [],\n'
            '  "next_steps": []\n'
            "}"
        )
    ]

    return "\n".join(prompt)