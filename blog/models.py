from django.db import models
from django.contrib.auth.models import User

OPCIONES_SECCION = (
    ("Novedades", "Novedades"),
    ("Varios", "Varios"),
    ("Curiosidades", "Curiosidades"),
    ("Ficcion", "Ficcion"),
)


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, default="")
    seccion = models.CharField(
        max_length=20,
        choices=OPCIONES_SECCION,
        default='Novedades'
    )
    cuerpo = models.TextField(max_length=5000)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.TextField(max_length=200, default="")
    referencia = models.URLField(max_length=200)

    def __str__(self):
        return f'{self.titulo} de {self.autor}'


class BlogComments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comentario} de {self.user}'
