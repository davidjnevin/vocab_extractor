import glob
import sqlite3
import argparse


from vocab_extractor.extract import extract_vocabulary
from vocab_extractor.io_utils import create_database, insert_words, read_file, clear_vocabulary_table
from vocab_extractor.vocab_cli import parse_args, check_db_name

batch_size = 2


def process_reports(report_files: list[str], conn: sqlite3.Connection) -> None:
    unique_word_pos_pairs = set()
    word_pos_pairs_to_insert = []

    for file_path in report_files:
        print(f"Processing file: {file_path}")
        content = read_file(file_path)
        vocabulary = extract_vocabulary(content)

        for word, pos in vocabulary:
            if (word, pos) not in unique_word_pos_pairs:
                unique_word_pos_pairs.add((word, pos))
                word_pos_pairs_to_insert.append((word, pos))

    insert_words(word_pos_pairs_to_insert, conn)


    # def batch_files(report_files: list[str], batch_size: int = 2) -> list[str]:
    # for i in range(0, len(report_files), batch_size):
    #    yield report_files[i: i + batch_size]


def process_all_reports(report_files: list[str], conn: sqlite3.Connection, batch_size: int) -> None:
    for idx in range(0, len(report_files), batch_size):
        batch = report_files[idx:idx + batch_size]
        process_reports(batch, conn)
        print(f"Processed batch {idx/batch_size}")


def parse_args():
    parser = argparse.ArgumentParser(description="Extract vocabulary from reports and store them in a database.")
    parser.add_argument("--batch-size", type=int, default=100, help="The number of documents to process in each batch (default: 100)",)
    parser.add_argument(
        "--db-name",
        type=str,
        default="vocabulary.db",
        help="The name of the SQLite database file to store the vocabulary (default: vocabulary.db)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    batch_size = args.batch_size
    db_name = args.db_name

    # Check if the database file already exists and prompt the user if necessary
    db_name = check_db_name(db_name)

    doc_files = glob.glob("./reports/**/*.doc", recursive=True)
    docx_files = glob.glob("./reports/**/*.docx", recursive=True)
    report_files = doc_files + docx_files

    with create_database(db_name) as conn:
        clear_vocabulary_table(conn)
        process_all_reports(report_files, conn, batch_size)


if __name__ == "__main__":
    main()
