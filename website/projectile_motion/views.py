from django.shortcuts import render
from .forms import ProjectileMotionForm
from .models import ProjectileMotionData
from .utils import projectile_motion_simulation

def index(request):
    initial_data = ProjectileMotionData.objects.first()
    if request.method == 'POST':
        form = ProjectileMotionForm(request.POST, instance=initial_data)
        if form.is_valid():
            form.save()
            projectile_motion_simulation(request)
    else:
        form = ProjectileMotionForm(instance=initial_data)
    return render(request, 'projectile_motion/index.html', {'form': form})