# books/models.py

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)

class Item1(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True)



class Item3(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
