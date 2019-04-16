from django import forms
from django.views.generic.edit import UpdateView
from .models import Prestamo, Genero
from .forms import *

class PrestamoForm(forms.ModelForm):
    
    class Meta:
        model = Prestamo
        fields = '__all__'