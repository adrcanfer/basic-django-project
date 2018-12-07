from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response
from music import models
from django.template import RequestContext

# Create your views here.
from music.forms import CancionForm, GeneroForm, AutorForm


def index(request):
    return render(request, 'index.html')


def canciones(request):
    canciones = models.Cancion.objects.all()
    return render(request, 'canciones.html', {'canciones': canciones})


def cantantes(request):
    cantantes = models.Autor.objects.all()
    return render(request, 'cantantes.html', {'cantantes': cantantes})


def generos(request):
    generos = models.Genero.objects.all()
    return render(request, 'generos.html', {'generos': generos})


def create_cancion(request):
    if request.method=='POST':
        formulario = CancionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/canciones")
    else:
        formulario = CancionForm()

    return render(request, 'create.html', {'formulario': formulario})


def create_genero(request):
    if request.method == 'POST':
        formulario = GeneroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/generos")
    else:
        formulario = GeneroForm()

    return render(request, 'create.html', {'formulario': formulario})


def create_autor(request):
    if request.method == 'POST':
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/cantantes")
    else:
        formulario = AutorForm()

    return render(request, 'create.html', {'formulario':formulario})


