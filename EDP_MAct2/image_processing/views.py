from django.shortcuts import render

from .utils import image_prediction

from .forms import ImageDocument
from .models import Image

# Create your views here.
def index(request):
    return render(request, "image_processing/index.html")

def upload_image(request):
    if request.method == 'POST':
        form = ImageDocument(request.POST, request.FILES)

        if form.is_valid():
            image_file = Image(docfile=request.FILES['docfile'])
            file_name = request.FILES['docfile']
            image_file.save()

            prediction = image_prediction.predict_upload_image(file_name)

            return render(request, "image_processing/upload.html", {
                "form": form,
                "category": prediction['category'],
                "accuracy": prediction['accuracy']
            })

    return render(request, 'image_processing/upload.html', {
        "form": ImageDocument()
    })