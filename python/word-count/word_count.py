import re
from collections import Counter

def word_count(phrase):
    phrase = phrase.lower()
    phrased = re.findall(r"[A-Za-z\d]+", phrase)
    return dict(Counter(phrased))
    