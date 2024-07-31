"""
Implementar un CRUD (Create, Read, Update, Delete) básico para un modelo, por ejemplo, un modelo Producto. Definir el modelo Producto en models.py con campos como nombre, descripción y precio. Usar vistas basadas en clases (Class-Based Views) como ListView, DetailView, CreateView, UpdateView y DeleteView.  Crear formularios con ModelForm. Configurar las rutas y plantillas necesarias.
"""

### 1. Definir el modelo `Producto` en `models.py`:

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

### 2. Crear el formulario con ModelForm, en myapp/forms.py:

from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

### 3. Configurar las vistas basadas en clases (Class-Based Views), en myapp/views.py:

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')


### 4. Configurar las rutas en `urls.py`, en myapp/urls.py:

from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('<int:pk>/borrar/', ProductoDeleteView.as_view(), name='producto_delete'),
]

### 5. Crear htmls, en `myapp/templates`:

#### `index.html`

<!DOCTYPE html>
<html>
<head>
    <title>Página Principal</title>
</head>
<body>
    <h1>Bienvenido a la Página Principal</h1>
    <a href="{% url 'producto_list' %}">Ver Productos</a>
</body>
</html>

#### `producto_list.html`

<!DOCTYPE html>
<html>
<head>
    <title>Lista de Productos</title>
</head>
<body>
    <h1>Lista de Productos</h1>
    <a href="{% url 'producto_create' %}">Crear Producto</a>
    <ul>
        {% for producto in object_list %}
            <li>
                <a href="{% url 'producto_detail' producto.pk %}">{{ producto.nombre }}</a> - {{ producto.precio }}
                <a href="{% url 'producto_update' producto.pk %}">Editar</a>
                <a href="{% url 'producto_delete' producto.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
    <br>
    <a href="{% url 'index' %}">Volver a la página de inicio</a>
</body>
</html>

#### `producto_detail.html`

<!DOCTYPE html>
<html>
<head>
    <title>Detalle del Producto</title>
</head>
<body>
    <h1>{{ object.nombre }}</h1>
    <p>{{ object.descripcion }}</p>
    <p>{{ object.precio }}</p>
    <a href="{% url 'producto_update' object.pk %}">Editar</a>
    <a href="{% url 'producto_delete' object.pk %}">Eliminar</a>
    <a href="{% url 'producto_list' %}">Volver a la lista</a>
</body>
</html>

#### `producto_form.html`

<!DOCTYPE html>
<html>
<head>
    <title>{% if object %}Editar{% else %}Crear{% endif %} Producto</title>
</head>
<body>
    <h1>{% if object %}Editar{% else %}Crear{% endif %} Producto</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">{% if object %}Actualizar{% else %}Crear{% endif %}</button>
    </form>
    <a href="{% url 'producto_list' %}">Volver a la lista</a>
</body>
</html>

#### `producto_confirm_delete.html`

<!-- myapp/templates/producto_confirm_delete.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Eliminar Producto</title>
</head>
<body>
    <h1>Eliminar Producto</h1>
    <p>¿Estás seguro de que deseas eliminar el producto "{{ object.nombre }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Sí, eliminar</button>
    </form>
    <a href="{% url 'producto_list' %}">Cancelar</a>
</body>
</html>

### 6. Configurar las URLs del proyecto, en project/urls.py:

from django.contrib import admin
from django.urls import path, include
from myapp.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('myapp.urls')),
    path('', index, name='index'),  
]

### 7. Migrar los cambios a la base de datos:

python manage.py makemigrations
python manage.py migrate

### 8. Ejecutar el servidor

python manage.py runserver

### 9. Prueba:

Acceder a la ruta:

http://127.0.0.1:8000/