from django.contrib import admin
from .models import Prestamo, Genero

# Register your models here.

admin.site.register(Prestamo)
admin.site.register(Genero)