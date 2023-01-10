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

# Servidor de desarrollo

Navegar hasta la ubicación de `manage.py` y ejecutar:
```
python manage.py runserver
```
El servidor abre por defecto en `http://localhost:8000/`

# Crear una app

0. Parar el servidor de desarrollo con `Ctrl + C`
1. Navegamos hasta la ubicación de `manage.py` y ejecutamos:
2. Crear app:
```
python manage.py startapp <nombre_de_tu_app>
```
3. Deberías ver una carpeta con el nombre `<nombre_de_tu_app>`

# Añadir un HTML

Seguir los pasos de [este tutorial](https://www.w3schools.com/django/django_templates.php)

1. Crear `templates` en la carpeta de la app
2. Crear `index.html` o algún HTML en la carpeta `templates`
3. Actualizamos `views.py`:
```python
from django.template import loader
from django.http import HttpResponse

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())
```
4. Actualizamos `settings.py`:
```python
INSTALLED_APPS = [
    ...
    '<nombre_de_carpeta_de_app>'
    ]
```
5. Ejecutamos la migración:
```
python manage.py migrate
```
6. Ejecutamos el servidor de desarrollo:
```
python manage.py runserver
```

## Creamos tabla en la base de datos

[Más información](https://www.w3schools.com/django/django_models.php)

**models.py**

```python
from django.db import models

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
```
- Crea migración: 
```
python manage.py makemigrations members
```
- Ejecuta migración:
```
python manage.py migrate
```
- Ver SQL para crear tabla:
```
python manage.py sqlmigrate members 0001
```
**SQLite3**
- Para ver las tablas en SQLite3, 
A. Desde el `shell` con sqlite3 `<nombre_de_base_de_datos>` -> `.tables`
B. Abrir plugin de SQLite3 en VSCode -> Quick Query -> elegir base de datos y ejecutamos:
```
SELECT name FROM sqlite_master WHERE type='table';
```
Veremos algo como:
```
...
members_member
```
o en mi caso:
```
...
hello_world_app_member
```
**Importante:** No se modifican las tablas de Django.

## Insertar datos en la base de datos

[Más información](https://www.w3schools.com/django/django_insert_data.php)

- Abrimos el shell interactivo de Python y Django:
```
python manage.py shell
```
- Importamos el modelo:
```python
from <nombre_de_la_app>.models import Member
```
* nombre_de_la_app: nombre de la carpeta de la app -> `members` o en mi caso `hello_world_app`

- Creamos un objeto:
```python
member = Member(id=1, firstname='John', lastname='Doe')
```
- Guardamos el objeto:
```python
member.save()
```
- Verificamos que se guardó:
```python
Member.objects.all().values()
```