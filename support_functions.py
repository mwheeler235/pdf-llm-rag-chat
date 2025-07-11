import re
import PyPDF2
import tiktoken
from langchain_core.documents import Document

"""
Support Functions for RAG System
"""

def split_into_subtitle_sections(pdf_path):
    """
    Splits a PDF into Subtitle sections based on subtitle patterns.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        list: A list of Document objects, each representing a subtitle section with its 
              text content and subtitle number metadata.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        documents = pdf_reader.pages

        # Concatenate text from all pages
        text = " ".join([doc.extract_text() for doc in documents])

        # Split text into subtitles based on subtitle title pattern
        subtitles = re.split(r'(Subtitle\s[A-Z]+(?:\s[A-Z]+)*)', text)

        # Create Document objects with subtitle metadata
        subtitle_docs = []
        subtitle_num = 1
        for i in range(1, len(subtitles), 2):
            subtitle_text = subtitles[i] + subtitles[i + 1]  # Combine title and content
            doc = Document(page_content=subtitle_text, metadata={"Subtitle": subtitle_num})
            subtitle_docs.append(doc)
            subtitle_num += 1

    return subtitle_docs

def replace_double_lines_with_one_line(text):
    """
    Replaces consecutive double newline characters ('\n\n') with a single newline character ('\n').

    Args:
        text (str): The input text string.

    Returns:
        str: The text string with double newlines replaced by single newlines.
    """
    cleaned_text = re.sub(r'\n\n', '\n', text)
    return cleaned_text