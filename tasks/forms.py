from django import forms
from .models import *

class TaskFrom(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'