from django.forms import ModelForm
from .models import Task, Fav


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'importante']


class Fav(ModelForm):
    class Meta:
        model = Fav
        fields = ['nombre', 'tipo', 'claves', 'url']
