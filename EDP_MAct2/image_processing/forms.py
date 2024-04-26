from django import forms

class ImageDocument(forms.Form):
    docfile = forms.FileField(label="")