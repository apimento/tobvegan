from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Cat: 
    def __init__(self, name, breed, description, age):
        self.name = name 
        self.breed = breed 
        self.age = age 
        self.description = description 
        self.age = age 

cats = [ 
    Cat('Lolo' , "Tabby", "foul little demon", 3),
    Cat('Sachi', "Tortoise Shell", "diluted tortoise shell", 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]

def home(request): 
    return HttpResponse('<h1> Cat Collector </h1>') 

def about(request): 
    return render(request, 'about.html') 

def restaurants_index(request): 
    return render(request, 'restaurants/index.html', {'cats': cats})