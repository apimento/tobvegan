from django.urls import path
from django.urls import URLPattern 
from . import views 

urlpatterns = [ 
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('restaurants/', views.restaurants_index, name="index"),
    path("restaurants/<int:restaurant_id>/", views.restaurants_details, name='detail')
]