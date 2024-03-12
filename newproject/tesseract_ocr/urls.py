from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tts/", views.text_to_speech, name="tts")
]
