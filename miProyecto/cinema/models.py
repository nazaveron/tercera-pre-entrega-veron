from django.db import models

class movie(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField()
    def __str__(self):
        return self.titulo
class usuario(models.Model):
    email = models.EmailField(primary_key=True)
    edad = models.PositiveIntegerField()
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    def __str__(self):
        return self.apellido, self.email
    
class ReservaPelicula(models.Model):
    pelicula = models.ForeignKey(movie, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    sala = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    entradas_disponibles = models.PositiveIntegerField()


class WatchList(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    año_lanzamiento = models.IntegerField()
    def __str__(self):
        return self.titulo