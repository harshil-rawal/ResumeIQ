from pathlib import Path
from utils.parser import extract_text_from_pdf

UPLOADS = Path("uploads")

pdf_files = list(UPLOADS.glob("*.pdf"))

assert pdf_files, "No PDF files found in uploads/"

pdf_path = pdf_files[0]

text = extract_text_from_pdf(str(pdf_path))

print(text)