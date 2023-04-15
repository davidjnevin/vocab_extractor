import sqlite3

from vocab_extractor.io_utils import (clear_vocabulary_table, create_database,
                                      insert_words)


def test_create_database(tmp_path):
    db_file = tmp_path / "test.db"
    with create_database(db_file) as conn:
        assert conn is not None
        assert isinstance(conn, sqlite3.Connection)
        assert db_file.is_file()


def test_insert_words(tmp_path):
    db_file = tmp_path / "test.db"
    with create_database(db_file) as conn:
        words = [("hello", "NN"), ("world", "NN"), ("test", "NN")]
        insert_words(words, conn)
        cur = conn.cursor()
        cur.execute("SELECT word, pos FROM vocabulary")
        result = cur.fetchall()
        assert set(result) == {("hello", "NN"), ("world", "NN"), ("test", "NN")}


def test_clear_vocabulary_table(tmp_path):
    db_file = tmp_path / "test.db"
    with create_database(db_file) as conn:
        words = [("hello", "NN"), ("world", "NN"), ("test", "NN")]
        insert_words(words, conn)
        clear_vocabulary_table(conn)
        cur = conn.cursor()
        cur.execute("SELECT word, pos FROM vocabulary")
        result = cur.fetchall()
        assert len(result) == 0
