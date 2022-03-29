from django.urls import path
from django.urls import URLPattern 
from . import views 

urlpatterns = [ 
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('restaurants/', views.restaurants_index, name="index"),
    path("restaurants/<int:restaurant_id>/", views.restaurants_details, name="detail"),
    path('cats/<int:pk>/update/', views.RestaurantUpdate.as_view(), name="restaurant_update"),
    path('cats/<int:pk>/delete/', views.RestaurantDelete.as_view(), name="restaurant_delete"),
    path('cats/<int:restaurant_id>/add_menuHighlight', views.add_menuHighlight, name="add_menuHighlight") 
]