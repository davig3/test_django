from curses import meta
from dataclasses import fields
from django import forms
from .models import Tarea


# "This is a form that will be used to create or update a Tarea object."
# 
# The Meta class tells Django which model should be used to create this form (model = Tarea)
class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ['tarea']