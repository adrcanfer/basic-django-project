#encoding:utf-8
from django.forms import ModelForm
from music.models import Cancion, Genero, Autor


class CancionForm(ModelForm):
    class Meta:
        model = Cancion
        fields = '__all__'


class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'


class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

