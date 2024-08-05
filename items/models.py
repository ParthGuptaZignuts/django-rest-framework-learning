from django.db import models
# Create your models here

class Insaan(models.Model):
    username = models.CharField(max_length=20)
    email    = models.EmailField()
    password = models.CharField(max_length=15)

class Items(models.Model):
    item_name        = models.TextField(max_length=100)
    item_description = models.TextField(max_length=255)

