import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

pdf_path = "resumes.pdf"   
resume_text = extract_text_from_pdf(pdf_path)


with open("resume_text.txt", "w", encoding="utf-8") as file:
    file.write(resume_text)

print("Resume text successfully saved to requirements.txt")
