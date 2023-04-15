# Vocab Extractor (Early Beta Tokenizer)

Vocab Extractor is a Python script that processes Microsoft Word documents and extracts unique words and their part of speech (POS) tags. The extracted words and POS tags are then saved in an SQLite database.

## Functionality

The script follows these steps:

1. Read Word documents (.docx files) from a specified directory
2. Extract the text content from each document
3. Tokenize the text using the nltk library
4. Determine the POS tags for each token
5. Store the unique words and their POS tags in an SQLite database

## Test Suite

A comprehensive test suite is available to test the functionality of the Vocab Extractor. The test suite covers the following areas:

- Extracting vocabulary from text
- Reading file contents
- Creating a database connection
- Inserting words into the database
- Processing reports
- Batching files
- Processing all reports

To run the tests, make sure you have `pytest` installed:

