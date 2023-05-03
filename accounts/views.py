from django.shortcuts import render
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import ProfileEditForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your views here.


class user_edit_profile(UpdateView):
    model = Profile
    template_name = 'accounts/user_edit_profile.html'
    fields = ['image', 'location', 'bio', 'interests']
    success_url = '/mi_profile/'


@login_required
def user_edit_profile(request):
    usuario = request.user
    if request.method == 'POST':
        form = ProfileEditForm(
            request.POST, request.FILES, instance=usuario.profile)
        if form.is_valid():
            data = form.cleaned_data
            if 'image' in request.FILES:
                image = request.FILES['image']
                filename = default_storage.save(
                    image.name, ContentFile(image.read()))
                usuario.profile.image = filename
            usuario.profile.interests.set(data['interests'])
            usuario.profile.location = data['location']
            usuario.profile.bio = data['bio']
            usuario.save()
            form = ProfileEditForm(instance=usuario.profile)
            return render(request, 'accounts/user_edit_profile.html', {'form': form, 'mensaje1': 'Se han actualizado los datos correctamente.'})
        else:
            form = ProfileEditForm(instance=usuario.profile)
            return render(request, 'accounts/user_edit_profile.html', {'form': form, 'error1': 'Por favor, verifique los datos ingresados'})
    else:
        form = ProfileEditForm(instance=usuario.profile)
        print(form)
        return render(request, 'accounts/user_edit_profile.html', {'form': form})


@login_required
def mi_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {'profile_user': user})
