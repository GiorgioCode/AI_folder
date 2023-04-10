from django.contrib import admin
from .models import Tareas
# Register your models here.


class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ("creado",)


admin.site.register(Tareas, TareaAdmin)
