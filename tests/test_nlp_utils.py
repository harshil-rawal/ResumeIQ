from utils.nlp_utils import generate_all_ngrams

tokens = [
    "python",
    "machine",
    "learning",
    "tensorflow"
]

ngrams = generate_all_ngrams(tokens)

for gram in sorted(ngrams):
    print(gram)