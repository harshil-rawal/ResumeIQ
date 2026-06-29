#generate n-grams
def generate_all_ngrams(tokens, max_n=3):
    """
    Generate all n-grams from size 1 to max_n.
    """

    ngrams = set()

    for n in range(1, max_n + 1):

        for i in range(len(tokens) - n + 1):

            phrase = " ".join(tokens[i:i+n])

            ngrams.add(phrase)

    return ngrams