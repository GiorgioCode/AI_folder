from django.forms import ModelForm
from .models import BlogComments, Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'seccion',
                  'cuerpo', 'imagen', 'referencia']


class CommentForm(ModelForm):
    class Meta:
        model = BlogComments
        fields = ['comentario']
