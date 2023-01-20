from django.http import HttpResponse
from django.views import View

variable_global = "Esto es un string global"

class MyView(View):
    necesita_self = "Esto es un string en la clase"
    variable_en_clase = "Este contenido no saldrá en la respuesta"
    def get(self, request):
        no_necesita_self = "Esto es un string en el método"
        return HttpResponse(f"{variable_global}. {self.necesita_self}. {no_necesita_self}. {self.variable_en_clase}.")

class SubClaseView(MyView):
    variable_en_clase = "String desde subclase"
    def get(self, request):
        return HttpResponse(f"Hola desde subclase.")
    
# Ejemplo con animales y perros y gatos
class Animal(View):
    animal = "Animal"
    sonido = "Sonido del animal"
    def get(self, request):
        return HttpResponse(f"{self.animal}: {self.sonido}")
class Perro(Animal):
    animal = "Perro"
    sonido = "Guau"
class Gato(Animal):
    animal = "Gato"
    sonido = "Miau"
        
        
