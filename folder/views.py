
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import AnotarForm


def home(request):
    return render(request, 'home.html')


def folder(request):
    return render(request, 'folder.html')


def user_signup(request):
    if request.method == 'GET':
        return render(request, 'user_signup.html', {'form': UserCreationForm, 'estado': ""})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('folder')
            except IntegrityError:
                return render(request, 'user_signup.html', {'form': UserCreationForm, 'error1': True})
        else:
            return render(request, 'user_signup.html', {'form': UserCreationForm, 'error2': True})


def user_signin(request):
    if request.method == "GET":
        return render(request, 'user_login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user_login.html', {'form': AuthenticationForm, 'error': True})
        else:
            login(request, user)
            return redirect('folder')


def user_signout(request):
    logout(request)
    return redirect('home')


def anotar(request):
    return render(request, 'folder.html', {'form': AnotarForm})


def mi_tasks(request):
    return render(request, 'mi_tasks.html')


def mi_apps(request):
    return render(request, 'mi_apps.html')


def mi_notes(request):
    return render(request, 'mi_notes.html')


def detail_task(request):
    return render(request, 'detail_tasks')


def detail_app(request):
    return render(request, 'detail_app')


def detail_note(request):
    return render(request, 'detail_notes')


def create_task(request):
    return render(request, 'create_task')


def create_app(request):
    return render(request, 'create_app')


def create_note(request):
    return render(request, 'create_note')
