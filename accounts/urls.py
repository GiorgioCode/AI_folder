from django.urls import path

from .views import *

urlpatterns = [
    path("user_edit_profile/", user_edit_profile,
         name="user_edit_profile"),
    path("mi_profile/", mi_profile, name="mi_profile")
]
