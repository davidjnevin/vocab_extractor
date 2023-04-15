from vocab_extractor.extract import extract_vocabulary


def test_extract_vocabulary():
    text = "This is a sample text. It contains some words, punctuation, and numbers like 1234."
    expected_result = {
        ("this", "DT"),
        ("is", "VBZ"),
        ("a", "DT"),
        ("sample", "JJ"),
        ("text", "NN"),
        ("it", "PRP"),
        ("contains", "VBZ"),
        ("some", "DT"),
        ("words", "NNS"),
        ("punctuation", "NN"),
        ("and", "CC"),
        ("numbers", "NNS"),
        ("like", "IN"),
    }
    assert extract_vocabulary(text) == expected_result
