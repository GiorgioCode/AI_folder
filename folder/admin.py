from django.contrib import admin
from .models import Task, Fav

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', )


admin.site.register(Task, TaskAdmin)
admin.site.register(Fav)
