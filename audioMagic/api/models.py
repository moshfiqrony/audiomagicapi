
from django.db import models

# Create your models here.


class Magic(models.Model):
    name = models.CharField(max_length=150, null=True)
    audioFile = models.FileField(null=True)