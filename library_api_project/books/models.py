from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 255)
    publisher = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    quantity = models.IntegerField()
    genre = models.CharField(max_length = 255)