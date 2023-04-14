from vocab_extractor.extract import extract_vocabulary

def test_extract_vocabulary():
    text = "This is a sample text. It contains some words, punctuation, and numbers like 1234."
    expected_result = {"This", "is", "a", "sample", "text", "It", "contains", "some", "words", "punctuation", "and", "numbers", "like", "1234"}
    assert extract_vocabulary(text) == expected_result

