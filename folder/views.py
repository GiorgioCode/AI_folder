from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm, 'estado': ""})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return render(request, 'signup.html', {'form': UserCreationForm, 'estado': "Se registró el usuario correctamente", 'estilo': 'color:green'})
            except:
                return render(request, 'signup.html', {'form': UserCreationForm, 'estado': "El nombre de usuario ya se encuentra registrado", 'estilo': 'color:red'})

        else:
            return render(request, 'signup.html', {'form': UserCreationForm, 'estado': "Las contraseñas no coinciden.", 'estilo': 'color:red'})
