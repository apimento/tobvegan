from django.urls import path
from django.urls import URLPattern 
from . import views 

urlpatterns = [ 
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('restaurants/', views.restaurants_index, name="index"),
    path("restaurants/<int:restaurant_id>/", views.restaurants_details, name="detail"),
    path("restaurants/create", views.RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name="restaurant_update"),
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name="restaurant_delete"),
    path('restaurants/<int:restaurant_id>/add_menuHighlight', views.add_menuHighlight, name="add_menuHighlight"),   
    path('restaurants/<int:restaurant_id>', views.delete_Menuhighlight, name="delete_menuhighlight"),

    #URL for signup 
    path('accounts/signup/', views.signup, name="signup")

]