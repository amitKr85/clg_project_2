from PIL import Image
from pytesseract import image_to_string
#pytesseract.pytesseract.tesseract_cmd = 'F:\Tesseract-OCR\\tesseract.exe'

#pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

print(image_to_string(Image.open('developers_ss.png')))