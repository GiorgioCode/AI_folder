from django.urls import path

from .views import *

urlpatterns = [
    path("", blog, name="blog"),
    path('delete_blog/<pk>/', delete_blog.as_view(), name='delete_blog'),
    path('detail_blog/<int:blog_id>/', detail_blog, name='detail_blog'),
    path('create_blog/', create_blog.as_view(), name='create_blog'),
    path('update_blog/<pk>/', update_blog.as_view(), name='update_blog')
]
