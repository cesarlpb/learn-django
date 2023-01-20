# learn-django
Repositorio para aprender Django

# Instalación de Django

Para instalar Django ver [este tutorial](https://docs.djangoproject.com/es/4.1/topics/install/).

## Tutorial de Django

Empezamos el tutorial de la documentación de Django, [Parte 1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/).

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

2. Configurando la base de datos
Continuamos con la [Parte 2](https://docs.djangoproject.com/en/4.1/intro/tutorial02/).

- Para cambiar zona horaria vamos a `mysite/settings.py` y cambiamos `TIME_ZONE = 'UTC'` por `TIME_ZONE = 'Europe/Madrid'`
- Hacemos la migración para Django:
```
python manage.py migrate
```
- Creamos modelos `Question` y `Choice` en `polls/models.py`
- Añadimos la app `polls`en `mysite/settings.py` en `INSTALLED_APPS`:
```
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ...
    ]
```
- Creamos migraciones para los modelos:
```
python manage.py makemigrations polls
```
- Revisamos el SQL de la migración:
```
python manage.py sqlmigrate polls 0001
```
- Aplicamos la migración:
```
python manage.py migrate
```
### Insertando datos en la base de datos
- Abrimos el shell:
```
python manage.py shell
```
- Seguimos estos pasos para insertar datos desde el shell: [consola de Django](https://docs.djangoproject.com/es/4.1/intro/tutorial02/#playing-with-the-api)

## Panel admin
- Crear superuser:
```
python manage.py createsuperuser
```
**Nota:** Podéis poner mismo admin y password para el entorno de dev de cada proyecto o app... El email se puede dejar en blanco presionando `Enter`.

- Ejecutamos la app y vamos a `/admin`:
```
python manage.py runserver
```
- Importamos modelo `Question` en `polls/admin.py`:
```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
