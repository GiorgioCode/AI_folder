# Generated by Django 4.2 on 2023-04-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='users/robot_avatar.png', null=True, upload_to='avatares'),
        ),
    ]
