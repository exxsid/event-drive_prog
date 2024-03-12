from django.shortcuts import render

from PIL import Image
import pytesseract
from gtts import gTTS

# Create your views here.


def index(request):
    image_path = 'tesseract_ocr/static/images.png'
    image = Image.open(image_path)

    extracted_text = pytesseract.image_to_string(image, lang='eng')

    return render(request, "tesseract_ocr/index.html", {
        "extracted_text": extracted_text,
        "file_name": "images.png"
    })


def text_to_speech(request):
    image_path = 'tesseract_ocr\static\images.png'
    image = Image.open(image_path)

    extracted_text = pytesseract.image_to_string(image, lang="eng")

    tts = gTTS(extracted_text, lang="en")
    tts.save('tesseract_ocr/static/audio.mp3')

    return render(request, "tesseract_ocr/tts.html", {
        "extracted_text": extracted_text,
        "file_name": "plap.jpg",
        "audio_name": "audio.mp3"
    })
