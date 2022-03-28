from django.db import models

# Create your models here.

class Restaurant(models.Model): 
    name = models.CharField(max_length=100) 
    pricePoint= models.CharField (max_length=6)  
    contact=models.CharField(max_length=200)
    style=models.CharField(max_length=100) 
    menuHighlights = models.CharField(max_length=200) 
    delivery= models.BooleanField()
    events = models.BooleanField()
