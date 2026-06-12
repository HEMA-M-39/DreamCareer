from app.services.pdf_parser import extract_text_from_pdf, clean_text

pdf_path = "sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)
text = clean_text(text)

print(text)