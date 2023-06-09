from django.contrib import admin
from .models import Task, Fav, Comments

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', )


admin.site.register(Task, TaskAdmin)
admin.site.register(Fav)
admin.site.register(Comments)


admin.site.site_header = 'AI Folder'
admin.site.site_title = 'Panel de Administracion'
