import glob
import sqlite3

from vocab_extractor.extract import extract_vocabulary
from vocab_extractor.io_utils import create_database, read_file, insert_word

batch_size = 2


def process_reports(report_files: list[str], conn: sqlite3.Connection) -> None:
    for file_path in report_files:
        print(f"Processing file: {file_path}")
        content = read_file(file_path)
        vocabulary = extract_vocabulary(content)

        for word, pos in vocabulary:
            insert_word(word, pos, conn)


def batch_files(report_files: list[str], batch_size: int = 2) -> list[str]:
    for i in range(0, len(report_files), batch_size):
        yield report_files[i : i + batch_size]


def process_all_reports(report_files: list[str], conn: sqlite3.Connection, batch_size: int = 2) -> None:
    for idx, batch in enumerate(batch_files(report_files, batch_size), start=1):
        process_reports(batch, conn)
        print(f"Processed batch {idx}")


def main() -> None:
    db_name = "vocabulary_token_1.db"
    conn = create_database(db_name)
    doc_files = glob.glob("./reports/**/*.doc", recursive=True)
    docx_files = glob.glob("./reports/**/*.docx", recursive=True)
    report_files = doc_files + docx_files
    process_all_reports(report_files, conn)
    conn.close()


if __name__ == "__main__":
    main()
