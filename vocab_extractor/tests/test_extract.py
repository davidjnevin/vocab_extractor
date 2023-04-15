from vocab_extractor.extract import extract_vocabulary


def test_extract_vocabulary():
    content = "Hello, world! Test document"
    extracted_vocab = extract_vocabulary(content)
    expected_vocab = {
        ("hello", "NN"),
        ("world", "NN"),
        ("test", "NN"),
        ("document", "NN"),
    }
    assert extracted_vocab == expected_vocab
