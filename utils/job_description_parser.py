from utils.preprocessing import preprocess_text
from utils.nlp_utils import generate_all_ngrams
from utils.skills import extract_skills

def parse_job_description(job_description: str):
    """
    Parse a job description and extract categorized skills.

    Parameters:
        job_description (str): Raw job description text.

    Returns:
        dict: Extracted skills grouped by category.
    """
    # Step 1: Preprocess text
    tokens = preprocess_text(job_description)

    # Step 2: Generate n-grams
    ngrams = generate_all_ngrams(tokens)

    # Step 3: Extract skills
    skills = extract_skills(ngrams)

    return skills    