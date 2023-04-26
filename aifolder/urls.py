from django.contrib import admin
from django.urls import path
from folder import views
from django.urls import path, re_path
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    # URLS DE MANEJO DE USUARIOS
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_login/', views.user_signin, name='user_login'),
    path('user_logout/', views.user_signout, name="user_logout"),
    # URLS DE TAREAS
    path('mi_tasks/', views.mi_tasks, name='mi_tasks'),
    path('mi_tasks/<int:task_id>/complete',
         views.complete_task, name='complete_task'),
    path('mi_tasks/<int:task_id>/delete',
         views.delete_task, name='delete_task'),
    path('create_task/', views.create_task, name='create_task'),
    path('mi_tasks/<int:task_id>', views.detail_task, name='detail_task'),
    # URLS DE FAVORITOS
    path('mi_favs/', views.mi_favs, name='mi_favs'),
    path('create_fav/', views.create_fav, name='create_fav'),
    path('detail_fav/<int:fav_id>/', views.detail_fav, name='detail_fav'),
    path('detail_mifav/<int:fav_id>', views.detail_mifav, name='detail_mifav'),
    path('delete_mifav/<pk>/', views.delete_mifav.as_view(), name='delete_mifav'),
]

handler404 = 'folder.views.error_404_view'
