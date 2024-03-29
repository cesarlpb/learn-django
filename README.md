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

## Comandos

Crear venv:
```
    python3 -m virtualenv venv
```
Activar venv en Mac/Linux:
```
    source venv/bin/activate
```
Activar venv en Windows:
```
    venv\Scripts\activate
```
Desactivar venv:
```
    deactivate
``` 
Instalar Django:
```
    pip install django
```

## PM2 

1. Copiar el archivo `pm2.json` a vuestro proyecto
2. Cambiar datos como `nombre de app`, `puerto`, etc.
3. Iniciar proceso:
```
    pm2 start pm2.json
```
4. Para mirar log:
```
    pm2 ls
```
y usando el id de la izquierda:
```
    pm2 log <id>
```
