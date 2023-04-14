from pathlib import Path

from docx import Document

from vocab_extractor.io_utils import read_file


def test_read_file(tmp_path: Path):
    # Create a temporary .docx file for testing
    temp_docx = tmp_path / "test.docx"
    doc = Document()
    doc.add_paragraph("This is a temporary file for testing.")
    doc.save(temp_docx)

    content = read_file(str(temp_docx))
    assert content.strip() == "This is a temporary file for testing."
