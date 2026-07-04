import os
import pdfplumber
from datetime import datetime


def get_file_info(filepath: str) -> dict:
    if not os.path.exists(filepath):
    raise FileNotFoundError(f"File not found: {filepath}")

    """
    Extract metadata from a resume PDF.
    """

    filename = os.path.basename(filepath)
    extension = os.path.splitext(filename)[1]
    filesize_kb = round(os.path.getsize(filepath) / 1024, 2)

    created_at = datetime.fromtimestamp(
        os.path.getctime(filepath)
    ).strftime("%Y-%m-%d %H:%M:%S")

    modified_at = datetime.fromtimestamp(
        os.path.getmtime(filepath)
    ).strftime("%Y-%m-%d %H:%M:%S")

    with pdfplumber.open(filepath) as pdf:

        pages = len(pdf.pages)

        metadata = pdf.metadata or {}

        encrypted = pdf.is_encrypted

    return {
        "filename": filename,
        "extension": extension,
        "filesize_kb": filesize_kb,
        "pages": pages,
        "created_at": created_at,
        "modified_at": modified_at,
        "encrypted": encrypted,
        "title": metadata.get("Title"),
        "author": metadata.get("Author"),
        "creator": metadata.get("Creator"),
        "producer": metadata.get("Producer"),
    }