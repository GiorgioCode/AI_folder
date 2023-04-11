from django.forms import ModelForm
from .models import Tareas


class AnotarForm(ModelForm):
    class Meta:
        model = Tareas
        fields = ['titulo', 'descripcion', 'fecha_limite', 'importante']
