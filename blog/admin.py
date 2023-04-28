from django.contrib import admin

# Register your models here.
from .models import Blog, BlogComments

admin.site.register(Blog)
admin.site.register(BlogComments)
