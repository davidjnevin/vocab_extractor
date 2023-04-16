# Vocab Extractor (Early Beta Tokenizer)

This version of the Vocabulary Extractor script processes a collection `.docx` files and extracts unique words and their corresponding Part of Speech (POS) tags. It saves the extracted (word, pos) pairs and cumulative word_count into an SQLite database.

## Features

- Tokenizes the document content using the NLTK library.
- Extracts Part of Speech (POS) information for each word.
- Efficiently inserts unique (word, pos, word_count) into an SQLite database using batch inserts and in-memory data structure.
- Includes a test suite to ensure the functionality of the script.
- Command line interface for easy execution and configuration

## Test Suite

A comprehensive test suite is available to test the functionality of the Vocab Extractor. The test suite covers the following areas:

- Extracting vocabulary from text
- Reading file contents
- Creating a database connection
- Inserting words into the database
- Processing reports
- Batching files
- Processing all reports
- Command line interface inputs

To run the tests, make sure you have `pytest` installed:

