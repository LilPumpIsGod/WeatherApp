from .models import City
from django.froms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        field = ['name']


