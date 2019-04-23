from PIL import Image
import pytesseract

def core(filename):
    text = pytesseract.image_to_string(Image.open(filename))

    return text

print(core("D:\\Ohjelmointi\\Python\\python-projects\\OCRtesting\\pic.jpg"))
