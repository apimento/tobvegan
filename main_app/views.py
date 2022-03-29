from django.http import HttpResponse
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import Restaurant 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .forms import MenuHighlightsForm

# Create your views here.

# class Restaurant: 
#     def __init__(self, name, contact, pricePoint, style, menuHighlights, delivery, events):
#         self.name = name 
#         self.contact = contact 
#         self.pricePoint = pricePoint  
#         self.style = style
#         self.menuHighlights = menuHighlights  
#         self.delivery = delivery 
#         self.events = events

# restaurants = [ 
# ]

class RestaurantCreate(CreateView): 
    model = Restaurant 
    fields = '__all__'

def home(request): 
    return HttpResponse('<h1> T.O b Vegan </h1>') 

def about(request): 
    return render(request,'about.html') 

def restaurants_index(request): 
    restaurants =  Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {'restaurants': restaurants}) 

def restaurants_details(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id) 
    return render (request, 'restaurants/detail.html', {'restaurant': restaurant}) 

def add_menuHighlight(request, restaurant_id): 
    form = MenuHighlightsForm(request.POST) 
    if form.is_valid(): 
        new_menuHighlight = form.save(commit=False)
        new_menuHighlight.restaurant_id = restaurant_id
        new_menuHighlight.save()
    return redirect('detail', restaurant_id=restaurant_id)

class RestaurantUpdate(UpdateView): 
    model = Restaurant 
    fields = '__all__' 

class RestaurantDelete(DeleteView): 
    model = Restaurant 
    success_url = '/restaurants/'
