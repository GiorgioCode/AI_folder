
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import TaskForm, FavForm
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import DetailView, View, ListView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404, JsonResponse


def home(request):
    return render(request, 'home.html')

# Manejo de usuarios


def error_404_view(request, exception):
    return render(request, 'error_404.html')


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
                return redirect('home')
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
            return redirect('home')


@login_required
def user_signout(request):
    logout(request)
    return redirect('home')

# Manejo de tareas


@login_required
def mi_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'mi_tasks.html', {"tasks": tasks})


@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'detail_task.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('mi_tasks')
        except ValueError:
            return render(request, 'detail_task.html', {'task': task, 'form': form, 'error': 'Error updating task.'})


@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('mi_tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": TaskForm, "error": "Error creando la tarea"})


@login_required
def detail_task(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'detail_task.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('mi_tasks')
        except ValueError:
            return render(request, 'detail_task.html', {'task': task, 'form': form, 'error': 'Error actualizando la tarea'})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.save()
        return redirect('mi_tasks')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('mi_tasks')
# Manejo de favoritos


@login_required
def mi_favs(request):
    favs = Fav.objects.filter(user=request.user)

    return render(request, 'mi_favs.html', {"favs": favs})


class detail_fav(DetailView):
    model = Fav
    template_name = 'detail_fav.html'
    context_object_name = 'fav'


def detail_mifav(request, fav_id):
    if request.method == 'GET':
        fav = get_object_or_404(Fav, pk=fav_id, user=request.user)
        form = FavForm(instance=fav)
        return render(request, 'detail_mifav.html', {'fav': fav, 'form': form})
    else:
        try:
            fav = get_object_or_404(Fav, pk=fav_id, user=request.user)
            form = FavForm(request.POST, instance=fav)
            form.save()
            return redirect('mi_favs')
        except ValueError:
            return render(request, 'detail_mifav.html', {'fav': fav, 'form': form, 'error': 'Error actualizando la tarea'})


class delete_mifav(DeleteView):
    model = Fav
    template_name = 'delete_mifav.html'
    success_url = '/mi_favs'
    context_object_name = 'fav'


@login_required
def create_fav(request):
    if request.method == "GET":
        return render(request, 'create_fav.html', {"form": FavForm})
    else:
        try:
            form = FavForm(request.POST)
            new_fav = form.save(commit=False)
            new_fav.user = request.user
            new_fav.save()
            return redirect('mi_favs')
        except ValueError:
            return render(request, 'create_fav.html', {"form": FavForm, "error": "Error al crear el favorito"})
    return render(request, 'create_fav.html')


def explore(request):
    favs = Fav.objects.all()
    cheatsheets = favs.filter(tipo__icontains="CheatSheet")
    cantidad_cheatsheets = cheatsheets.count()
    webs = favs.filter(tipo__icontains="Web")
    cantidad_webs = webs.count()
    aplicaciones = favs.filter(tipo__icontains="Aplicacion")
    cantidad_aplicaciones = aplicaciones.count()
    apuntes = favs.filter(tipo__icontains="Apunte")
    cantidad_apuntes = apuntes.count()
    modelos = favs.filter(tipo__icontains="Modelo")
    cantidad_modelos = modelos.count()
    varios = favs.filter(tipo__icontains="Varios")
    cantidad_varios = varios.count()
    return render(request, 'explore.html', {"cheatsheets": cheatsheets, 'cantidad_cheatsheets': cantidad_cheatsheets, 'webs': webs, 'cantidad_webs': cantidad_webs, 'aplicaciones': aplicaciones, 'cantidad_aplicaciones': cantidad_aplicaciones, 'apuntes': apuntes, 'cantidad_apuntes': cantidad_apuntes, 'modelos': modelos, 'cantidad_modelos': cantidad_modelos, 'varios': varios, 'cantidad_varios': cantidad_varios})
