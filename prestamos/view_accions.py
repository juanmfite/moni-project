from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Prestamo, Genero
from .forms import PrestamoForm
from django.contrib.auth.decorators import login_required
import requests, environ
from django.contrib import messages

env = environ.Env()

@login_required
def administrador(request):
    '''
    Sitio de administracion.

    '''
    prestamos = Prestamo.objects.all()
    return render(request, 'admin.html', locals())


def index(request):
    '''
    Sitio principal que toma el formulario del prestamo.

    '''
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            if valid(form):
                post = form.save(commit=False)
                post.save()
                messages.success(request,'Prestamo exitoso!')
                return redirect('index')
            messages.success(request,'No se pudo realizar el prestamo')
            return redirect('index')
    if request.method == "GET":
        form = PrestamoForm()
    return render(request, 'index.html', {'form': form})

def valid(form):
    '''
    Funcion que consulta a la API de Moni y retorna si es
    posible realizar el prestamo o no como boolean.

    '''
    base = env.str("API_MONI")
    dni = 'document_number='+str(form.cleaned_data['dni'])
    genero = 'gender='+str(form.cleaned_data['genero'])
    email = 'email='+form.cleaned_data['email']
    url = base+dni+'&'+genero+'&'+email
    r = requests.get(url)
    r = r.json()
    if r['approved']:
        return True
    return False

@login_required
def deletePrestamo(request,pk):
    '''
    Boton para eliminar un prestamo en base a su pk.

    '''
    Prestamo.objects.filter(pk=pk).delete()
    return redirect('administrador')

@login_required
def prestamo_edit(request,pk):
    '''
    Boton para editar un prestamo en base a su pk.

    '''
    
    prestamo = Prestamo.objects.get(pk=pk)
    if request.method == "POST":
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.save()
            return redirect('administrador')
    else:
        form = PrestamoForm(instance=prestamo)

    return render(request, 'formEdit.html', {'form': form})