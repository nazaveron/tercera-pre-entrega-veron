from django.shortcuts import render
from django.http import HttpResponse
from cinema.models import *
from cinema.forms import *
def homepage(request):
    return render(request, "cinema/inicio.html")

def peliculas(request):

    pelicula = movie(titulo="Bastardos sin gloria", genero="Bélico/acción", director="Quentin Tarantino", duracion=153)
    pelicula.save()

    return HttpResponse(f"la peli es {pelicula.titulo}")

def user(request):
        return render(request, "cinema/iniciarSesion.html")

def funciones(request):
        return render(request, "cinema/funciones.html")


def Registrarse(request):
    if request.method == "POST":
        formulario_registro = Registro_usuario(request.POST)

        if formulario_registro.is_valid():
            info = formulario_registro.cleaned_data
            nuevo_usuario = usuario(
                nombre=info["nombre"],
                email=info["email"],
                apellido=info["apellido"],
                edad=info["edad"]
            )
            nuevo_usuario.save()
            return render(request, 'cinema/inicio.html')
    
    else:
        formulario_registro = Registro_usuario()
    
    return render(request, 'cinema/registrarse.html', {"form1": formulario_registro})


""" def buscarPelicula(request):

    return render(request, "cinema/buscarPelicula.html")

def resultados(request):
        
        if request.GET['movie']:
    
            movie = request.GET["movie"]
            peli_busqueda = movies.objects.filter(movies__icontains=pelicula)

            return render(request, 'cinema/resultados.html', {"peli_busqueda": peli_busqueda})
        
        else:
            respuesta = "No enviaste datos."

        return HttpResponse(respuesta) """




def buscar_pelicula(request):
    form = BusquedaPeliculaForm()
    return render(request, "cinema/busqueda.html", {"form": form})

def resultados(request):
    if request.method == 'GET':
        term = request.GET.get('movie', '')
        peliculas_encontradas = movie.objects.filter(titulo__icontains=term)

        return render(request, 'cinema/resultados.html', {"peliculas_encontradas": peliculas_encontradas})
    

