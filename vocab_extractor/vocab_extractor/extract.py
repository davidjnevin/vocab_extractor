import re
from typing import Set

def extract_vocabulary(text: str) -> Set[str]:
    words = set(re.findall(r"\b\w+\b", text))
    return words

