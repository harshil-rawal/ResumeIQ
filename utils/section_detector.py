SECTION_KEYWORDS = {
    "summary": [
        "summary",
        "professional summary",
        "profile",
        "objective",
        "career objective"
    ],
    "education": [
        "education",
        "academic background",
        "qualification",
        "qualifications"
    ],
    "experience": [
        "experience",
        "work experience",
        "employment",
        "professional experience"
    ],
    "projects": [
        "projects",
        "academic projects",
        "personal projects"
    ],
    "skills": [
        "skills",
        "technical skills",
        "core competencies"
    ],
    "certifications": [
        "certifications",
        "certificates",
        "licenses"
    ],
    "achievements": [
        "achievements",
        "awards",
        "accomplishments"
    ]
}

def detect_sections(raw_text):
    text = raw_text.lower()

    detected = {}

    for section, keywords in SECTION_KEYWORDS.items():
        detected[section] = any(
            keyword in text
            for keyword in keywords
        )

    return detected

def extract_section_positions(raw_text):
    """
    Return the starting line number of detected section headings.
    """

    positions = {}

    lines = raw_text.splitlines()

    for line_number, line in enumerate(lines):

        line = line.strip().lower()

        for section, keywords in SECTION_KEYWORDS.items():

            if section in positions:
                continue

            if line in keywords:
                positions[section] = line_number

    return positions