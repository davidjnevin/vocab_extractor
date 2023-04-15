import sqlite3
import pytest
from pathlib import Path

from vocab_extractor.io_utils import create_database, insert_word


def test_create_database(tmp_path: Path):
    temp_db = tmp_path / "test.db"
    conn = create_database(str(temp_db))
    assert isinstance(conn, sqlite3.Connection)


def test_insert_word(tmp_path: Path):
    temp_db = tmp_path / "test.db"
    conn = create_database(str(temp_db))
    word = "test"
    pos = "NN"
    insert_word(word, pos, conn)
    cursor = conn.execute("SELECT word, pos FROM vocabulary WHERE word=? AND pos=?", (word, pos))
    assert cursor.fetchone() == (word, pos)

