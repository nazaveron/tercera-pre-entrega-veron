from django.shortcuts import render

def homepage(request):
    return render(request, "cinema/inicio.html")

def registrarse(request):
    return render(request, "cinema/registrarse.html")