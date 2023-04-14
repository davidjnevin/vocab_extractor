import glob
import re
import sqlite3
from typing import List, Set


def extract_vocabulary(file_content: str) -> Set[str]:
    """Extract unique vocabulary words from a given file content."""
    pattern = re.compile(r"\b\w+\b")
    return set(pattern.findall(file_content))


def create_database(db_name: str) -> sqlite3.Connection:
    """Create a SQLite database and vocabulary table."""
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(
        """
    CREATE TABLE IF NOT EXISTS vocabulary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT UNIQUE
    )"""
    )
    conn.commit()
    return conn


def insert_word(conn: sqlite3.Connection, word: str) -> None:
    """Insert a unique vocabulary word into the database."""
    c = conn.cursor()
    try:
        c.execute("INSERT OR IGNORE INTO vocabulary (word) VALUES (?)", (word,))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting word '{word}': {e}")


def process_reports(report_files: List[str], conn: sqlite3.Connection) -> None:
    """Process the report files and extract unique vocabulary words."""
    for report_file in report_files:
        with open(report_file, "r", encoding="utf-8") as file:
            content = file.read()
            vocab_words = extract_vocabulary(content)

            for word in vocab_words:
                insert_word(conn, word)


def main(max_files: int = 10) -> None:
    db_name = "vocabulary.db"
    conn = create_database(db_name)
    report_files = glob.glob('../reports/**/*.[dD][oO][cC]*', recursive=True)
    report_files = report_files[:max_files]  # Limit number of files to process
    process_reports(report_files, conn)
    conn.close()


if __name__ == "__main__":
    main()
