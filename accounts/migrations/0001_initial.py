# Generated by Django 4.2 on 2023-04-30 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'Interes',
                'verbose_name_plural': 'Intereses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='users/robot_avatar.png', upload_to='users/')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, max_length=300, null=True)),
                ('interests', models.ManyToManyField(blank=True, null=True, to='accounts.interest', verbose_name='Intereses')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['-id'],
            },
        ),
    ]
