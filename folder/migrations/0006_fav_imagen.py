# Generated by Django 4.2 on 2023-04-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0005_remove_canalmensaje_canal_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fav',
            name='imagen',
            field=models.URLField(default='', max_length=250),
        ),
    ]
