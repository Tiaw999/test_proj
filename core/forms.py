from django import forms
from django.forms import ModelForm
from .models import Data, Play

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        widgets = {
            'exhibit': forms.Select(),  # Ensure this is a dropdown
            'plays_seen': forms.CheckboxSelectMultiple(),
        }
