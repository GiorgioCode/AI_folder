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
