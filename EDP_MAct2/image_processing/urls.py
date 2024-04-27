from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload_image, name="upload"),
    path("capture/", views.capture_image, name="capture"),
    path("capture/classify-captured/", views.captured_image_classifier, name="classifier"),
    path("real-time/", views.real_time_prediction, name="real-time"),
    path("real-time/classify-captured/", views.captured_image_classifier, name="classifier"),
]