from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    creado = models.DateTimeField(auto_now_add=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.user}'


OPCIONES_TIPOS = (
    ("Apunte", "Apunte"),
    ("CheatSheet", "CheatSheet"),
    ("Aplicacion", "Aplicacion"),
    ("Modelo", "Modelo"),
    ("Web", "Web"),
    ("Varios", "Varios")
)


class Fav(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=20,
        choices=OPCIONES_TIPOS,
        default='Aplicacion'
    )
    claves = models.CharField(max_length=100)
    url = models.URLField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.user}'
