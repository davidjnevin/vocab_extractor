import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description="Extract vocabulary from reports and store them in a database.")
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="The number of documents to process in each batch (default: 100)",
    )
    parser.add_argument(
        "--db-name",
        type=str,
        default="vocabulary.db",
        help="The name of the SQLite database file to store the vocabulary (default: vocabulary.db)",
    )
    return parser.parse_args()


def check_db_name(db_name):
    while os.path.exists(db_name):
        print(f"Warning: The specified database '{db_name}' already exists. Overwriting it will result in data loss.")
        user_input = input("Enter 'c' to continue and overwrite, or provide a new database name: ").strip()
        if user_input.lower() == "c":
            break
        elif user_input != "":
            db_name = user_input
    return db_name
