from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    email = models.CharField(max_length=200)