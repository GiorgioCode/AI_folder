from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tareas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField(null=True)
    importante = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario} - {self.titulo}'


class Aplicacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    claves = models.CharField(max_length=100)
    url = models.URLField(max_length=250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.usuario}'


class Apunte(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    claves = models.CharField(max_length=100)
    url = models.URLField(max_length=250)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre} - {self.usuario}'
