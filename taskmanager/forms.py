from django import forms
from .models import Task

class createform(forms.ModelForm):
    
    class Meta:
            
        model=Task
        fields = ['Name','description','status']