from django import forms
from .models import Destination

class DestinationForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField(required=False)