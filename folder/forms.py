from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from .models import Task, Fav, Comments
from django import forms
from django.contrib.auth.models import User


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


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comentario']


class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="", widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
