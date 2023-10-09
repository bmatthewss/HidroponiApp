import os

from django.db import models
import re
from django.core.exceptions import ValidationError


# Create your models here.

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.srt', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


class FileSRTUpload(models.Model):
    file = models.FileField(upload_to='subtitulosGPT/files/received', validators=[validate_file_extension])
    #filename = file.name
    idiomaTarget = models.CharField(max_length=30)

    def __str__(self):
        return self.file.name

class Service(models.Model):
    name = models.CharField(max_length=30)
    pid = models.IntegerField()

    def __str__(self):
        return self.file.name

class Languages(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.file.name