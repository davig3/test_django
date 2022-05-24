from django.shortcuts import redirect, render
from .models import Tarea
from .forms import TareaForm

# Create your views here.

def home(request):
    """
    The function home() takes a request as an argument, and returns a rendered template called home.html
    
    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: The home function is returning the render function.
    """
    tareas = Tarea.objects.all()
    context = {'tareas':tareas}
    return render(request, 'todo/home.html',context)


def agregar(request):
    """
    If the request is a POST request, then we create a form with the data from the request. If the form
    is valid, we save it to the database and redirect the user to the home page. If the request is not a
    POST request, then we create an empty form and render it in the template
    
    :param request: The request is an HttpRequest object. It contains metadata about the request
    :return: The form is being returned.
    """
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context = {'form':form}
    return render(request, 'todo/agregar.html',context)

def eliminar(request, tarea_id):
    """
    It gets the task with the given id, deletes it, and then redirects to the home page
    
    :param request: The request object is an HttpRequest object. It contains metadata about the request
    :param tarea_id: The id of the task to be deleted
    :return: the redirect function, which is a shortcut to the HttpResponseRedirect class.
    """
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')

def editar(request, tarea_id):
    """
    We get the task we want to edit, then we check if the request is a POST request, if it is, we get
    the data from the form and save it, if it's not, we just show the form
    
    :param request: The request is an HttpRequest object. It contains metadata about the request
    :param tarea_id: This is the id of the task that we want to edit
    :return: The form is being returned.
    """
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm(instance=tarea)
    context = {'form' : form}
    return render(request, 'todo/editar.html', context)