import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")


def to_lowercase(text):
    """
    Convert text to lowercase.
    """
    return text.lower()


def normalize_spaces(text):
    """
    Remove extra spaces and newlines.
    """
    return " ".join(text.split())


def preprocess_text(text):
    """
    Complete preprocessing pipeline for ResumeIQ.
    """

    # Step 1
    text = to_lowercase(text)

    # Step 2
    text = normalize_spaces(text)

    # Step 3
    doc = nlp(text)

    cleaned_tokens = []

    for token in doc:

        # Ignore stopwords
        if token.is_stop:
            continue

        # Ignore spaces
        if token.is_space:
            continue

        # Ignore empty tokens
        if token.text.strip() == "":
            continue

        # Keep punctuation inside technologies like C++, C#, Node.js
        lemma = token.lemma_.strip()

        if lemma:
            cleaned_tokens.append(lemma)

    return cleaned_tokens