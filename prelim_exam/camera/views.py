from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

import base64
import pytesseract
from PIL import Image
import io
import json
import gtts
import time

from .models import Document
from .forms import DocumentForm, TextInputForm

# Create your views here.


@csrf_exempt
def capture_image(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data.get('image_data')

        if image_data:
            image_bytes = base64.b64decode(image_data.split(',')[1])
            image = Image.open(io.BytesIO(image_bytes))

            # save the image
            image.save("camera/static/captured.png")
            return HttpResponse(status=200)


def index(request):
    if request.method == 'POST':
        try:
            image_path = 'camera\static\captured.png'
            image = Image.open(image_path)

            # convert image to text
            text = pytesseract.image_to_string(image)

            # convert text to audio
            tts = gtts.gTTS(text)
            tts.save("camera/static/audio-capture.mp3")

            time.sleep(1)

            return render(request, "index.html", {
                "text": text,
                "audio": "audio-capture.mp3",
                "photo": "captured.png"
            })
        except AssertionError:
            return render(request, "index.html", {
                "text": "Unable to convert",
                "photo": "captured.png"
            })

    return render(request, "index.html")


def file_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            image_file = Document(docfile=request.FILES['docfile'])

            image_file.save()

            image_path = f"camera/static/media/{request.FILES['docfile']}"
            image = Image.open(image_path)

            # convert image to text
            text = pytesseract.image_to_string(image)

            # convert text to audio
            tts = gtts.gTTS(text)
            tts.save("camera/static/audio-upload.mp3")

            time.sleep(1)

            return render(request, "upload.html", {
                "form": form,
                "text": text,
                "audio": "audio-upload.mp3",
                "photo": f"{request.FILES['docfile']}"
            })

    return render(request, "upload.html", {
        "form": DocumentForm()
    })


def text_input(request):
    if request.method == "POST":
        form = TextInputForm(request.POST)

        if form.is_valid():
            input_text = form.cleaned_data['text_input']

            # convert text to audio
            tts = gtts.gTTS(input_text)
            tts.save("camera/static/audio-textinput.mp3")

            time.sleep(1)

            return render(request, "input-text.html", {
                "form": form,
                "audio": "audio-textinput.mp3",
            })

    return render(request, "input-text.html", {
        "form": TextInputForm()
    })
