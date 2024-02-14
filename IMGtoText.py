import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Path to the tesseract

def convert(Image_path) :
    try:
        img = Image.open(Image_path)
        text = pytesseract.image_to_string(img)
        print(text)
    except Exception as e: 
        print("eror: ", e)

Image_path = r"C:\Users\Michael\Downloads\jomblo.jpg"
convert(Image_path)