from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=30)
    birthDate=models.DateTimeField()
    name = models.CharField(max_length=50)