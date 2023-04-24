# Generated by Django 4.2 on 2023-04-22 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('folder', '0003_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanalMensaje',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
                ('texto', models.TextField()),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folder.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanalUsuario',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
                ('canal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='folder.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='canal',
            name='usuarios',
            field=models.ManyToManyField(blank=True, through='folder.CanalUsuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
