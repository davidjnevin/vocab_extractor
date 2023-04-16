import glob
import os

import docx
import textract


def convert_doc_to_docx(doc_path, docx_path):
    # Extract text from .doc file
    text = textract.process(doc_path).decode("utf-8")

    # Create a new .docx file
    docx_file = docx.Document()

    # Add extracted text to the .docx file
    docx_file.add_paragraph(text)

    # Save the .docx file
    docx_file.save(docx_path)


def main():
    folder_path = './reports/'
    # Find all .doc files in the folder and its subfolders
    doc_files = glob.glob(os.path.join(folder_path, "**", "*.doc"), recursive=True)

    for doc_path in doc_files:
        docx_path = doc_path[:-4] + ".docx"
        print(docx_path)
        convert_doc_to_docx(doc_path, docx_path)
        print(f"Converted {doc_path} to {docx_path}")


if __name__ == "__main__":
    main()
