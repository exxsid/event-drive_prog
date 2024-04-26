from django.db import models

# Create your models here.
class Image(models.Model):
    docfile = models.FileField(upload_to="media/")