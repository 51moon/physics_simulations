from django.urls import path
from . import views

urlpatterns = [
    path('projectile_motion/', views.projectile_motion, name='projectile_motion'),
]