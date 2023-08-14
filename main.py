import pyttsx3
from PyPDF2 import PdfReader

with open('sample.pdf', 'rb') as file:
    pdf = PdfReader(file)
    number_of_pages = len(pdf.pages)

    for i, page_num in enumerate(range(number_of_pages)):
        page = pdf.pages[i]
        page_text = page.extract_text()
        engine = pyttsx3.init()
        engine.say(page_text)
        engine.say(f"end of page{i + 1}")
        engine.runAndWait()
