from typing import Set

from nltk import pos_tag
from nltk.tokenize import word_tokenize


def extract_vocabulary(text: str) -> Set[tuple[str, str]]:
    lowercase_text = text.lower()
    # Tokenize the text
    tokens = word_tokenize(lowercase_text)

    # Perform POS tagging
    tagged_tokens = pos_tag(tokens)

    # Create a set of unique (word, POS) tuples
    words = set((word, pos) for word, pos in tagged_tokens if word.isalpha())
    return words
