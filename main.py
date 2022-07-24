from importlib.resources import path
import eel
import pathlib
import os
from PIL import Image
from pytesseract import pytesseract

userProfile = os.path.expandvars("%userprofile%")

# Path to Tesseract.exe
path_to_tesseract = userProfile + r'\AppData\Local\Tesseract-OCR\tesseract.exe'

# Point tesseract_cmd to tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

imageFolder = str(pathlib.Path().resolve()) + "\web\img\\"

eel.init('web')


@eel.expose
def getText(imageName):
    print("Image name: " + imageName)
    pathImage = str(imageFolder) + imageName
    print("Path image: " + pathImage)

    # Open image with PIL
    img = Image.open(pathImage)

    # Extract text from image
    text = pytesseract.image_to_string(img)

    print("Text from image: " + text)
    return text


eel.start('index.html')
