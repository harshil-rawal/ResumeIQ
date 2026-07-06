from utils.parser import extract_text_from_pdf
from utils.preprocessing import preprocess_text
from utils.nlp_utils import generate_all_ngrams
from utils.skills import extract_skills, generate_skill_statistics
from utils.ats import calculate_ats_score
from utils.ai_coach import generate_ai_feedback

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
    
    # Step 5: Extract skills statistics
    statistics = generate_skill_statistics(skills)
    
    ats = calculate_ats_score(
        raw_text,
        skills,
        statistics
    )
    
    ai_feedback = generate_ai_feedback(ats)

    # Return complete analysis
    return {
        "raw_text": raw_text,
        "tokens": tokens,
        "ngrams": list(ngrams),
        "skills": skills,
        "statistics": statistics,
        "ats": ats,
        "ai_feedback": ai_feedback["feedback"]
    }