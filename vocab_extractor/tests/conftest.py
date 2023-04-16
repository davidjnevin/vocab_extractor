import os

import pytest
from docx import Document


@pytest.fixture(scope="session")
def temp_docx_file(tmpdir_factory):
    # Create a temporary directory
    temp_dir = tmpdir_factory.mktemp("test_data")

    # Create a test document in the temporary directory
    docx_file = os.path.join(temp_dir, "test_docx.docx")
    doc = Document()
    doc.add_paragraph("Hello, world! This is a test document.")
    doc.save(docx_file)

    return docx_file
