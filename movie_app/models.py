from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField()
    year=models.CharField(max_length=255)
    img=models.ImageField(upload_to='pic')