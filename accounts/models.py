from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class Interest(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='nombre')

    class Meta:
        verbose_name = 'Interes'
        verbose_name_plural = 'Intereses'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(
        upload_to='users', default='users/robot_avatar.png', null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=300, null=True, blank=True)
    interests = models.ManyToManyField(
        Interest, verbose_name='Intereses')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return f'{self.user}'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
