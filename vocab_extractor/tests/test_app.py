import os
import sqlite3

from vocab_extractor.app import process_all_reports


def test_process_all_reports(tmp_path, temp_docx_file):
    db_file = tmp_path / "test.db"
    with sqlite3.connect(db_file) as conn:
        conn.execute(
            """
            CREATE TABLE vocabulary (
                id INTEGER PRIMARY KEY,
                word TEXT,
                pos TEXT,
                UNIQUE(word, pos)
            )
        """
        )
        report_files = [os.path.join("tmp_path", temp_docx_file)]
        process_all_reports(report_files, conn, 1)
        cur = conn.cursor()
        cur.execute("SELECT word, pos FROM vocabulary")
        result = cur.fetchall()
        assert set(result) == {
            ("hello", "NN"),
            ("world", "NN"),
            ("this", "DT"),
            ("is", "VBZ"),
            ("a", "DT"),
            ("test", "NN"),
            ("document", "NN"),
        }
