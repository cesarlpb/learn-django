from django.contrib import admin
from .models import Animal, Publisher, Author, Book

admin.site.register(Animal)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)