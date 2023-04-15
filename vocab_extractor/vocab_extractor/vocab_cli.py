import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Vocabulary Extractor")
    parser.add_argument(
        "--batch_file",
        type=str,
        default="batch.txt",
        help="Path to the batch file containing paths to document files.",
    )
    parser.add_argument(
        "--db_name",
        type=str,
        default="vocabulary.db",
        help="Name of the SQLite database to store the extracted vocabulary.",
    )
    args = parser.parse_args()
    return args


def check_db_name(db_name):
    while os.path.exists(db_name):
        print(f"Warning: The specified database '{db_name}' already exists. Overwriting it will result in data loss.")
        user_input = input("Enter 'c' to continue and overwrite, or provide a new database name: ").strip()
        if user_input.lower() == "c":
            break
        elif user_input != "":
            db_name = user_input
    return db_name
