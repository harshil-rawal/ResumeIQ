from utils.parser import extract_text_from_pdf
from utils.preprocessing import preprocess_text
from utils.nlp_utils import generate_all_ngrams
from utils.skills import extract_skills


def analyze_resume(filepath):
    """
    Complete Resume Analysis Pipeline.
    """

    # Step 1: Extract text from PDF
    raw_text = extract_text_from_pdf(filepath)

    # Step 2: Preprocess text
    tokens = preprocess_text(raw_text)

    # Step 3: Generate n-grams
    ngrams = generate_all_ngrams(tokens)

    # Step 4: Extract skills
    skills = extract_skills(ngrams)

    # Return complete analysis
    return {
        "raw_text": raw_text,
        "tokens": tokens,
        "ngrams": list(ngrams),
        "skills": skills
    }