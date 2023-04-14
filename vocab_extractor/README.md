# Vocabulary Extractor (Early Beta)

This script extracts unique vocabulary words from a collection of English class reports in `.doc` and `.docx` formats. It stores the extracted vocabulary words in a SQLite database.

## Functionality

The script performs the following tasks:

1. Recursively searches for `.doc` and `.docx` files in the `reports` folder.
2. Reads the content of each file using the `python-docx` library.
3. Extracts vocabulary words from the file content using regular expressions.
4. Creates a SQLite database to store the unique vocabulary words.
5. Inserts the extracted vocabulary words into the database, ignoring duplicates.
6. Processes files in batches of 100 to efficiently handle a large number of files.

## Testing

The script includes a test suite that tests the individual functions. To run the tests, make sure you have `pytest` installed:

