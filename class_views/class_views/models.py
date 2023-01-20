from django.db import models

# Ejemplo con animales 
class Animal(models.Model):
    name = models.CharField("Nombre", max_length=50)
    species = models.CharField("Especie", max_length=50)
    sound = models.CharField("Sonido", max_length=50)

    def __str__(self):
        return f"{self.species}: {self.name}"

# url https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/
# Ejemplo con Editorial, Autor y Libro
class Publisher(models.Model):
    name = models.CharField("Nombre", max_length=30)
    address = models.CharField("Dirección", max_length=50)
    city = models.CharField("Ciudad", max_length=60)
    state_province = models.CharField("Provincia", max_length=30)
    country = models.CharField("País", max_length=50)
    website = models.URLField("Sitio web")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField("Sr/Sra", max_length=10)
    name = models.CharField("Nombre", max_length=200)
    email = models.EmailField("Email")
    headshot = models.ImageField("Foto", upload_to='author_headshots')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField("Título", max_length=200)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField("Fecha de publicación")

    def __str__(self):
        return f"{self.title}"