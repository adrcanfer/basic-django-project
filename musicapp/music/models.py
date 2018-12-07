from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=50)
    anyo = models.IntegerField()
    autor = models.ForeignKey(Autor, null=True, on_delete=models.CASCADE)
    generos = models.ManyToManyField('Genero')

    def __str__(self):
        return self.titulo

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre