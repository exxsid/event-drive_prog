from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.file_upload, name="upload"),
    path("capture_image", views.capture_image, name="capture_image"),
    path("text-input/", views.text_input, name="text_input")
]
