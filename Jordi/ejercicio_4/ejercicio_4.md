### 2.JSON User List 

Descripción: Crear un endpoint que devuelva una lista de usuarios en formato JSON. Requisitos:

    Crear un modelo User.
    Poblar la base de datos con usuarios de prueba.
    Crear una vista que devuelva todos los usuarios en formato JSON.

### Paso 1: Configurar el proyecto Django

    django-admin startproject myproject
    cd myproject

## Crea una nueva aplicación dentro del proyecto.

    python manage.py startapp myapp

## Agrega la aplicación al archivo `settings.py` del proyecto.

    # myproject/settings.py
    INSTALLED_APPS = [
        ...
        'myapp',
    ]

### Paso 2: Crear el modelo `User` en myapp/models.py:

    from django.db import models

    class User(models.Model):
        username = models.CharField(max_length=100)
        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)

        def __str__(self):
            return self.username
## Aplicar las migraciones para crear la tabla `User` en la base de datos.

    python manage.py makemigrations
    python manage.py migrate

### Paso 3: Crear en la base de datos con usuarios de prueba

## shell de Django:

    python manage.py shell

## Añadir algunos usuarios de prueba.

    from myapp.models import User

    User.objects.create(username='jdoe', email='jdoe@example.com', first_name='John', last_name='Doe')
    User.objects.create(username='asmith', email='asmith@example.com', first_name='Anna', last_name='Smith')
    User.objects.create(username='bjones', email='bjones@example.com', first_name='Bob', last_name='Jones')

### Paso 4: Crear una vista que devuelva todos los usuarios en formato JSON, en myapp/views.py:

    from django.http import JsonResponse
    from .models import User

    def user_list(request):
        users = User.objects.all().values('username', 'email', 'first_name', 'last_name')
        users_list = list(users)
        return JsonResponse(users_list, safe=False)

## Configurar la URL para la vista en el archivo `urls.py` de la aplicación, en myapp/urls.py:

    from django.urls import path
    from .views import user_list

    urlpatterns = [
        path('users/', user_list, name='user_list'),
    ]

## Incluir URLs de la aplicación en el archivo `urls.py` del proyecto principal, en myproject/urls.py:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myapp.urls')),
    ]

### Paso 5: Probar

python manage.py runserver

Url `http://127.0.0.1:8000/users/` para ver una lista de usuarios en formato JSON.
