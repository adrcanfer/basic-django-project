from django.contrib import admin
from music.models import Cancion, Autor, Genero

# Register your models here.

admin.site.register(Cancion)
admin.site.register(Autor)
admin.site.register(Genero)
