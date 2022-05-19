from curses import meta
from dataclasses import fields
from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ['tarea']