HIGH = "high_priority"
MEDIUM = "medium_priority"
LOW = "low_priority"

SKILLS = "skills"
SECTIONS = "sections"
STRUCTURE = "structure"
TECHNICAL_PROFILE = "technical_profile"
READABILITY = "readability"

PLANNER_RULES = {

    SKILLS: {
        "threshold": 20,
        "priority": HIGH,
        "title": "Expand Technical Skills",
        "max_gain": 8
    },

    TECHNICAL_PROFILE: {
        "threshold": 8,
        "priority": HIGH,
        "title": "Strengthen Technology Stack",
        "max_gain": 6
    },

    SECTIONS: {
        "threshold": 14,
        "priority": MEDIUM,
        "title": "Complete Resume Sections",
        "max_gain": 5
    },

    STRUCTURE: {
        "threshold": 10,
        "priority": MEDIUM,
        "title": "Improve Resume Structure",
        "max_gain": 4
    },

    READABILITY: {
        "threshold": 7,
        "priority": LOW,
        "title": "Improve Readability",
        "max_gain": 3
    }
}

def create_suggestion(
    title,
    category,
    priority,
    estimated_gain,
    reason,
    actions
):
    """
    Create one ATS improvement suggestion.
    """

    return {
        "title": title,
        "category": category,
        "priority": priority,
        "estimated_gain": estimated_gain,
        "reason": reason,
        "actions": actions
    }
    
def generate_improvement_plan(
    scores,
    detected_domains
):
    """
    Generate ATS improvement plan.
    """

    plan = {
        HIGH: [],
        MEDIUM: [],
        LOW: []
    }

    for metric, rule in PLANNER_RULES.items():

        current_score = scores[metric]

        if current_score >= rule["threshold"]:
            continue

        estimated_gain = calculate_estimated_gain(
            current_score,
            rule["threshold"],
            rule["max_gain"]
        )

        suggestion = create_suggestion(
            title=rule["title"],
            category=metric.replace("_", " ").title(),
            priority=rule["priority"],
            estimated_gain=estimated_gain,
            reason=f"{metric.replace('_',' ').title()} score is below the recommended threshold.",
            actions=[]
        )

        plan[rule["priority"]].append(
            suggestion
        )
    
    for domain_name, domain in detected_domains.items():

        top_skills = get_top_missing_skills(domain)

        if not top_skills:
            continue

        actions = top_skills

        
        
        estimated_gain = sum(
            skill["weight"]
            for skill in top_skills
        )
        print(top_skills)
        suggestion = create_suggestion(
            title=f"Strengthen {domain_name} Skills",
            category=domain_name,
            priority=HIGH,
            estimated_gain=estimated_gain,
            reason=f"Your {domain_name} profile can be strengthened by learning these technologies.",
            actions=actions
        )

        plan[HIGH].append(suggestion)
    return plan
    
def calculate_estimated_gain(score, threshold, max_gain):
    """
    Calculate the estimated ATS gain based on how far the
    current score is from the target threshold.
    """

    if score >= threshold:
        return 0

    missing = threshold - score

    gain = round((missing / threshold) * max_gain)

    return max(1, gain)

def get_top_missing_skills(domain, limit=3):
    """
    Return the highest priority missing skills for a domain.
    """

    missing = domain.get("missing_skills", [])

    return missing[:limit]