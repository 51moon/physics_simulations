from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projectile_motion/", views.index, name="projectile_motion"),
]