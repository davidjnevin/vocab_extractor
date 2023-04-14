from docx import Document

def read_file(file_path: str) -> str:
    doc = Document(file_path)
    content = "\n".join([para.text for para in doc.paragraphs])
    return content

