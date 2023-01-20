from django.db import models

class Animal(models.Model):
    name = models.CharField("Nombre", max_length=50)
    species = models.CharField("Especie", max_length=50)
    sound = models.CharField("Sonido", max_length=50)

    def __str__(self):
        return f"{self.species}: {self.name}"
