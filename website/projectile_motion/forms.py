from django import forms
from .models import ProjectileMotionData

class ProjectileMotionForm(forms.ModelForm):
    class Meta:
        model = ProjectileMotionData
        fields = ['height', 'velocity', 'angle', 'mass', 'c_F', 'xmax', 'ymax']