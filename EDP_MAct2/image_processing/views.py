import io
from django.http import JsonResponse
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
                "category": prediction['category'].upper(),
                "accuracy": prediction['accuracy'] * 100,
                "photo": file_name
            })

    return render(request, 'image_processing/upload.html', {
        "form": ImageDocument()
    })

def capture_image(request):
    return render(request, "image_processing/capture.html")

def captured_image_classifier(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES.get('image')
        # Read the content of the uploaded file
        image_content = uploaded_image.read()
        # Create an in-memory file-like object from the content
        image_stream = io.BytesIO(image_content)
        
        result = image_prediction.predict_capture_image(image_stream)

        print(result)
        return JsonResponse({
            "category": result['category'],
            "accuracy": float(result['accuracy'])
        })
    else:
        return JsonResponse({'error': 'No image uploaded.'})
