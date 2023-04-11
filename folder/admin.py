from django.contrib import admin
from .models import Tareas, Aplicacion, Apunte
# Register your models here.


class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ("creado",)


admin.site.register(Tareas, TareaAdmin)
admin.site.register(Apunte)
admin.site.register(Aplicacion)
