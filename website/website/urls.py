from django.contrib import admin
from django.urls import include, path
from projectile_motion.utils import projectile_motion_simulation

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('projectile_motion_image', projectile_motion_simulation, name='projectile_motion_image'), # trajectory image path
    path('projectile_motion', include('projectile_motion.urls')),    
]