from django.shortcuts import render, redirect
from .forms import agregarTarea
# Create your views here.

tareas = []

def home(request):
    context = {'tareas' : tareas}
    return render(request, "todo/home.html", context)

def add(request):
    if request.method == 'POST':
        form = agregarTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            tareas.append(tarea)
            return redirect('home')
    else:
        form = agregarTarea()    
    context = {'form' : form}
    return render(request, "todo/add.html", context) 