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