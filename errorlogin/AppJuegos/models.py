from django.db import models

class Cargarlistadejuegos (models.Model):
    nombre=models.CharField(max_length=40)
    desarrollador=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    lanzamiento=models.DateField()
    puntuacion=models.IntegerField()# Create your models here.
        
    def __str__(self):
        return f"Nombre= : {self.nombre}"   



class Juegos (models.Model):

    nombre=models.CharField(max_length=40)
    desarrollador=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    lanzamiento=models.DateField()
    puntuacion=models.IntegerField()
    def __str__(self) -> str:
        return f"Juego : {self.nombre}"

    #para que en admin aparezca el nombre y no OBJECTS


class Altajuego(models.Model):
    nombre=models.CharField(max_length=40)
    desarrollador=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"Juego : {self.nombre}"
      



class Trucos(models.Model):
    juego=models.CharField(max_length=40)
    codigo=models.CharField(max_length=40)
    accion=models.CharField(max_length=40)
    def __str__(self):
        return f"Juego:  {self.juego}"   





