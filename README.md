# learn-django
Repositorio para aprender Django

# Instalación de Django

1. Crear entorno virtual y activarlo
2. Instalar Django: 
```
python -m pip install Django
```
3. Ver versión de Django:
```
python3 -m django --version
```
4. Crear proyecto:
```
django-admin startproject <nombre_de_tu_app> .
```
5. Deberías ver una carpeta con el nombre `<nombre_de_tu_app>`

## Tutorial de Django

Empezamos el tutorial de [documentación de Django](https://docs.djangoproject.com/en/4.1/intro/tutorial01/).

1. Primeros pasos. Creamos proyecto.
Archivos de mysite:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
Cambio del puerto para dev:
```
python manage.py runserver 8080
```
Creamos app `polls`:
```
python manage.py startapp polls
```

Archivos de polls:
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

