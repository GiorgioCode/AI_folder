from django.forms import ModelForm
from .models import Task, Fav
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion']


class FavForm(ModelForm):
    class Meta:
        model = Fav
        fields = ['nombre', 'descripcion', 'tipo', 'claves', 'url', 'imagen']

    def __init__(self, *args, **kwargs):
        super(FavForm, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False
