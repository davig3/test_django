from django import views
from django.urls import path
from . import views

# A list of url patterns.
urlpatterns = [

    path("", views.home, name="home"),
    path("agregar/", views.agregar, name="agregar"),
    path("eliminar/<int:tarea_id>/", views.eliminar, name="eliminar"),
    path("editar/<int:tarea_id>/", views.editar, name="editar"),

]