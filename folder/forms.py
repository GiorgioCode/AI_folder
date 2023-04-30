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


class PasswordEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="", widget=forms.HiddenInput(), required=False)

    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Repetir Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['password1', 'password2']

    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError(
                'Las contraseñas ingresadas no coinciden')
        return password2


class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="", widget=forms.HiddenInput(), required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
