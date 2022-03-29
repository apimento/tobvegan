from django.forms import ModelForm
from .models import MenuHighlights  

class MenuHighlightsForm(ModelForm): 
    class Meta: 
        model = MenuHighlights 
        fields = ['name' , 'image']