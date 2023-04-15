import sqlite3

from docx import Document


def insert_word(word: str, pos: str, conn: sqlite3.Connection) -> None:
    try:
        conn.execute("INSERT INTO vocabulary (word, pos) VALUES (?, ?)", (word, pos))
        conn.commit()
    except sqlite3.IntegrityError as err:
        print(f"Update Error - {err}")


def create_database(db_name: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_name)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS vocabulary (
                        id INTEGER PRIMARY KEY,
                        word TEXT NOT NULL,
                        pos TEXT NOT NULL,
                        UNIQUE (word, pos)
                    )"""
    )
    conn.commit()
    return conn


def read_file(file_path: str) -> str:
    doc = Document(file_path)
    content = "\n".join([para.text for para in doc.paragraphs])
    return content
