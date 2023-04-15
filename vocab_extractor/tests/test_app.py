import sqlite3
from pathlib import Path

from docx import Document

from vocab_extractor.app import (batch_files, create_database,
                                 process_all_reports, process_reports)


def test_create_database(tmp_path: Path):
    temp_db = tmp_path / "test.db"
    conn = create_database(str(temp_db))
    assert isinstance(conn, sqlite3.Connection)


def test_process_reports(tmp_path: Path):
    # Create a temporary .docx file for testing
    test_docx = tmp_path / "test.docx"
    doc = Document()
    doc.add_paragraph("This is a test document for process_reports.")
    doc.save(test_docx)

    temp_db = tmp_path / "test.db"
    conn = create_database(str(temp_db))
    report_files = [str(test_docx)]
    process_reports(report_files, conn)
    cursor = conn.execute("SELECT word FROM vocabulary")
    words = [row[0] for row in cursor.fetchall()]
    assert "test" in words


def test_batch_files():
    report_files = list(range(10))
    batch_gen = batch_files(report_files, batch_size=3)
    batches = [batch for batch in batch_gen]
    assert len(batches) == 4


def test_process_all_reports(tmp_path: Path):
    # Create a temporary .docx file for testing
    test_docx = tmp_path / "test.docx"
    doc = Document()
    doc.add_paragraph("This is a test document for process_all_reports.")
    doc.save(test_docx)

    temp_db = tmp_path / "test.db"
    conn = create_database(str(temp_db))
    report_files = [str(test_docx)]
    process_all_reports(report_files, conn)
    cursor = conn.execute("SELECT word FROM vocabulary")
    words = [row[0] for row in cursor.fetchall()]
    assert "test" in words
