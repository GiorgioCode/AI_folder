from django.contrib import admin
from django.urls import path, include
from folder import views
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

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
    path('about/', views.about, name='about'),
    path('mensajes/', include('Dm.urls')),
    path('pages/', include('blog.urls')),
    path('search/', views.search, name='search'),
    path('user_edit_profile/', views.user_edit_profile, name='user_edit_profile'),
    path('user_profile/<user_id>/', views.user_profile, name='user_profile'),

]

handler404 = 'folder.views.error_404_view'
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
