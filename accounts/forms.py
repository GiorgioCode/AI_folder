from django.forms import ModelForm
from .models import Profile


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'interests', 'location', 'bio']
