from django.forms import ModelForm
from .models import Profile, Interest
from django.forms import forms


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'location', 'bio']
