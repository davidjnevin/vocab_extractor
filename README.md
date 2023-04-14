# Vocabulary Extractor (Early Beta)

This Python script extracts unique vocabulary words from a collection of English class reports and stores them in a SQLite database.

## Overview

The Vocabulary Extractor script reads text files containing English class reports from a specified directory. It extracts unique vocabulary words from these files and stores them in a SQLite database, ensuring that each word has a unique ID.

The script consists of several functions:

- `extract_vocabulary(file_content: str) -> Set[str]`: Extracts unique vocabulary words from the given file content.
- `create_database(db_name: str) -> sqlite3.Connection`: Creates a SQLite database and a vocabulary table.
- `insert_word(conn: sqlite3.Connection, word: str) -> None`: Inserts a unique vocabulary word into the database.
- `process_reports(report_files: List[str], conn: sqlite3.Connection) -> None`: Processes the report files and extracts unique vocabulary words.
- `main() -> None`: The main function that brings everything together and executes the script.

## Usage

To use the Vocabulary Extractor, follow these steps:

1. Ensure that Python is installed on your system.
2. Place the `vocabulary_extractor.py` script in a directory containing the English class report files (with `.txt` extension).
3. Run the script using the command: `python vocabulary_extractor.py`
4. The extracted unique vocabulary words will be stored in a SQLite database called `vocabulary.db`.

