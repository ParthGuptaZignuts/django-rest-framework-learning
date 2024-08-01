from django.db import models


class Products(models.Model) :
    products_title = models.TextField(max_length=100)
    products_description = models.TextField(max_length=255)

# Create your models here.
