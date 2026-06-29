from utils.parser import extract_text_from_pdf

pdf_path = "uploads/Resume (4).pdf"   # Replace with your uploaded filename

text = extract_text_from_pdf(pdf_path)

print(text)