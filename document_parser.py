import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text(file):

    text = ""

    # Try normal extraction first
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    # If text extraction fails → OCR
    if len(text.strip()) < 50:
        print("OCR activated for scanned document")

        images = convert_from_bytes(file.read())

        for img in images:
            text += pytesseract.image_to_string(img)

    return text