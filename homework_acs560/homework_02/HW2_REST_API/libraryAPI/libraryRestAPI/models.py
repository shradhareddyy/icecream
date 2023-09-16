from django.db import models

class books (models.Model):
    bookTitle = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=50)
    bookPrice = models.CharField(max_length=10)
    
