from django.contrib import admin
from django.urls import include, path
from simulation.utils import simulation

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')),
    path('simulation_image', simulation, name='simulation_image'), # trajectory image path
    path('simulation', include('simulation.urls')),    
]
