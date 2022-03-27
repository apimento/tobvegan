from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Restaurant: 
    def __init__(self, name, contact, pricePoint, style, menuHighlights, delivery, events):
        self.name = name 
        self.contact = contact 
        self.pricePoint = pricePoint  
        self.style = style
        self.menuHighlights = menuHighlights  
        self.delivery = delivery 
        self.events = events

restaurants = [ 
]

def home(request): 
    return HttpResponse('<h1> T.O b Vegan </h1>') 

def about(request): 
    return render(request,'about.html') 

def restaurants_index(request): 
    return render(request, 'restaurants/index.html', {'restaurants': restaurants})