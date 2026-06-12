from pdf_parser import extract_text_from_pdf, clean_text

pdf_path = "app/services/sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)
text = clean_text(text)

print(text)