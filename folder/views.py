from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError


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
                login(request, user)
                return redirect('folder')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, 'error1': True})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm, 'error2': True})


def folder(request):
    return render(request, 'folder.html')


def signin(request):
    if request.method == "GET":
        return render(request, 'login.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form': AuthenticationForm, 'error': True})
        else:
            login(request, user)
            return redirect('folder')


def signout(request):
    logout(request)
    return redirect('home')
