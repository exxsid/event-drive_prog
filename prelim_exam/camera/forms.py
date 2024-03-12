from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='',
    )


class TextInputForm(forms.Form):
    text_input = forms.CharField(label="Text Input")
