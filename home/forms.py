from django import forms
from .models import Lecture

class ticket(forms.ModelForm):
    
    class Meta:
        model = Lecture
        fields = ('subject_name', 'faculty_name','batch')