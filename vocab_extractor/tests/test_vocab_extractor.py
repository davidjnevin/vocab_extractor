import os
import sqlite3
from vocab_extractor.app import extract_vocabulary, create_database, insert_word


def test_extract_vocabulary():
    sample_text = "The quick brown fox jumps over the lazy dog."
    expected_vocab = {'The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'}
    assert extract_vocabulary(sample_text) == expected_vocab


def test_create_database():
    test_db_name = 'test_vocabulary.db'
    if os.path.exists(test_db_name):
        os.remove(test_db_name)

    conn = create_database(test_db_name)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='vocabulary'")
    assert c.fetchone() is not None

    conn.close()
    os.remove(test_db_name)


def test_insert_word():
    test_db_name = 'test_vocabulary.db'
    if os.path.exists(test_db_name):
        os.remove(test_db_name)

    conn = create_database(test_db_name)
    test_word = 'example'
    insert_word(conn, test_word)

    c = conn.cursor()
    c.execute("SELECT word FROM vocabulary WHERE word=?", (test_word,))
    assert c.fetchone()[0] == test_word

    insert_word(conn, test_word)
    c.execute("SELECT COUNT(*) FROM vocabulary WHERE word=?", (test_word,))
    assert c

