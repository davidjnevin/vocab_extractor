import sqlite3
import pytest
from pathlib import Path

from vocab_extractor.io_utils import create_database, insert_words


def test_create_database(tmp_path: Path):
    temp_db = tmp_path / "test.db"
    conn = create_database(str(temp_db))
    assert isinstance(conn, sqlite3.Connection)


def test_insert_words(tmp_path: Path):
    temp_db = tmp_path / "test.db"
    conn = create_database(str(temp_db))
    words = [("test", "NN"), ("sample", "JJ")]
    insert_words(words, conn)

    cursor = conn.cursor()
    cursor.execute("SELECT word, pos FROM vocabulary")
    result = cursor.fetchall()

    assert len(result) == 2
    assert ("test", "NN") in result
    assert ("sample", "JJ") in result
