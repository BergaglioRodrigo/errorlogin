from django import forms


class Juegos_formulario(forms.Form):

    nombre=forms.CharField(max_length=40)
    desarrollador=forms.CharField(max_length=40)
    genero=forms.CharField(max_length=40)



class Formulario_listajuegos(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    desarrollador=forms.CharField(max_length=40)
    genero=forms.CharField(max_length=40)
    lanzamiento=forms.DateField()
    puntuacion=forms.IntegerField()    


class Formulario_trucos(forms.Form):
    
    juego=forms.CharField(max_length=40)
    codigo=forms.CharField(max_length=40)
    accion=forms.CharField(max_length=40)

