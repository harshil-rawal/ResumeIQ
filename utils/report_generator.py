"""
ATS Report Generator for ResumeIQ
"""
SKILLS = "skills"
SECTIONS = "sections"
STRUCTURE = "structure"
TECHNICAL_PROFILE = "technical_profile"
READABILITY = "readability"

STRONG_THRESHOLD = "strong"
WEAK_THRESHOLD = "weak"

STRENGTH = "strength"
WEAKNESS = "weakness"
WARNING = "warning"

REPORT_THRESHOLDS = {
    SKILLS: {
        STRONG_THRESHOLD: 30,
        WEAK_THRESHOLD: 20
    },

    SECTIONS: {
        STRONG_THRESHOLD: 16,
        WEAK_THRESHOLD: 10
    },

    STRUCTURE: {
        STRONG_THRESHOLD: 12,
        WEAK_THRESHOLD: 8
    },

    TECHNICAL_PROFILE: {
        STRONG_THRESHOLD: 10,
        WEAK_THRESHOLD: 6
    },

    READABILITY: {
        STRONG_THRESHOLD: 8,
        WEAK_THRESHOLD: 5
    }
}

REPORT_MESSAGES = {

    SKILLS: {
        STRONG_THRESHOLD: "Excellent technical skill coverage.",
        WEAK_THRESHOLD: "Technical skill coverage is limited."
    },

    SECTIONS: {
        STRONG_THRESHOLD: "Resume contains well-defined sections.",
        WEAK_THRESHOLD: "Important resume sections are missing."
    },

    STRUCTURE: {
        STRONG_THRESHOLD: "Resume follows a professional structure.",
        WEAK_THRESHOLD: "Resume formatting and organization can be improved."
    },

    TECHNICAL_PROFILE: {
        STRONG_THRESHOLD: "Technical profile demonstrates strong technology diversity.",
        WEAK_THRESHOLD: "Expand your technology stack to strengthen your technical profile."
    },

    READABILITY: {
        STRONG_THRESHOLD: "Resume is easy to read.",
        WEAK_THRESHOLD: "Improve readability using concise sentences and bullet points."
    }

}

REPORT_RULES = {
    SKILLS: WEAKNESS,
    SECTIONS: WEAKNESS,
    STRUCTURE: WARNING,
    TECHNICAL_PROFILE: WEAKNESS,
    READABILITY: WARNING
}

def create_report_item(metric, severity, score, message):
    """
    Create a structured ATS report item.
    """

    return {
        "metric": metric,
        "title": metric.replace("_", " ").title(),
        "severity": severity,
        "score": score,
        "message": message
    }

def evaluate_metric(report, metric, score, destination):
    """
    Evaluate one ATS metric and update the report.
    """

    thresholds = REPORT_THRESHOLDS[metric]
    messages = REPORT_MESSAGES[metric]

    if score >= thresholds[STRONG_THRESHOLD]:

        report[STRENGTH].append(
            create_report_item(
            metric,
            STRENGTH,
            score,
            messages[STRONG_THRESHOLD]
        )
    )

    elif score <= thresholds[WEAK_THRESHOLD]:

        report[destination].append(
            create_report_item(
                metric,
                destination,
                score,
                messages[WEAK_THRESHOLD]
            )
        )
        
        
def generate_report(scores):
    """
    Generate ATS report from score breakdown.
    """

    report = {
        STRENGTH: [],
        WEAKNESS: [],
        WARNING: []
    }

    for metric, destination in REPORT_RULES.items():

        evaluate_metric(
            report,
            metric,
            scores.get(metric, 0),
            destination
        )

    return report
