from django.db import models 
from django.urls import reverse  
from django.contrib.auth.models import User

# Create your models here. 

class Style(models.Model): 
    style = models.CharField(max_length= 200) 


class Restaurant(models.Model): 
    name = models.CharField(max_length=100) 
    pricePoint= models.CharField (max_length=6)   
    style=models.CharField (max_length=100)
    address= models.CharField (max_length=200)   
    mainInt = models.CharField (max_length=200) 
    phone= models.CharField(max_length=13)  
    webite= models.CharField(max_length=200) 
    Instagram = models.CharField(max_length=200)
    delivery= models.BooleanField()
    events = models.BooleanField()    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # style = models.ManyToManyField(Style)

    def get_absolute_url(self): 
        return reverse('detail', kwargs = {'restaurant_id': self.id}) 
    
    def __str__(self):
        return self.name


class MenuHighlights(models.Model): 
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200) 
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)