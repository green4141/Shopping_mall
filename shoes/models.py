from django.db import models

# Create your models here.

class Shoes(models.Model):
    subject = models.CharField(max_length=200)
    price = models.IntegerField()
    explain = models.CharField(max_length=500)
    img = models.ImageField(upload_to='photo/', default='photo/no_image.png')