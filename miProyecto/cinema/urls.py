from django.urls import path
from cinema.views import *

urlpatterns = [
    path('login/', user, name="User"),
    path('funciones/', funciones, name="Funciones"),
    path('registrarse/', Registrarse, name="Registro_Usuario"),
    path('buscarPelicula/', buscar_pelicula, name="buscar_pelicula"),
    path('resultados/', resultados, name="resultados")
    ]
