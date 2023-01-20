# learn-django
Repositorio para aprender Django

Rama para hacer CRUD con Class Based Views

## Creación de class_views

1. Creamos rama **sin historial**, como queremos basarla en rama `django_tutorial`, primero navegamos a dicha rama y hacemos `git pull` para confirmar que tenemos los cambios al díoa. Y luego creamos la rama `class_views`:

```
    git checkout django_tutorial
    git pull
```
```
    git checkout --orphan class_views
```

2. Activamos `venv` e intentamos levantar el servidor de desarrollo:

```
    python manage.py runserver
```

-> Si necesitamos resolver alguna configuración lo hacemos ahora.

* En `settings.py` como se pide el archivo `top_secret.txt`, en caso de que no lo encuentre debemos volverlo a crear con una llave privada para Django.

**Nota:** Este archivo no se trackea en el repositorio, por lo que cada quien debe crearlo en su máquina.

3. Creamos la app `class_views`:

```
    python manage.py startapp class_views
```

4. Realizamos las migraciones necesarias para la nueva app en el proyecto:
    
```
    python manage.py makemigrations
    python manage.py migrate
``` 

5. Volvemos a levantar el servidor de desarrollo y verificamos que todo funcione correctamente.
```
    python manage.py runserver
```

6. Crear superuser de nuevo porque la bbdd se creo nueva ya que no hemos hecho seguimiento de los cambios en la rama `django_tutorial` (a la bbdd):
```
    python manage.py createsuperuser
```

7. Hacer migraciones -> `makemigrations` y `migrate` para la nueva app `class_views`:
```
    python manage.py makemigrations class_views
    python manage.py migrate class_views
```

8. Quitamos algunos cambios previos de archivos de `mysite/templates` para que no salga lo de Polls (opcional)

9. Logeamos en `/admin` y debemos ver que no hay nada de `class_views` aun.

10. :)