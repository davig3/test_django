from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def moneda(request):
    num = 0
    context = {'num' : num}
    return render(request, 'hola/moneda.html', context)


def hola(request):
    return render(request,'hola/index.html')


def saludo(request, nombre):
    context = {'name' : nombre}
    return render(request, 'hola/saludo.html', context)