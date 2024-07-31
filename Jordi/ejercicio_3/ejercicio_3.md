### 1. API Data Fetching

Descripción: Crear un endpoint que haga una petición a una API externa, obtenga datos y los devuelva formateados en una lista. Requisitos:

    Usar requests para hacer la petición.
    Formatear los datos obtenidos.
    Devolverlos en formato JSON.

#### `views.py`

import requests
from django.http import JsonResponse

def fetch_data(request):
    # URL de la API externa
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    # Hacer la petición a la API externa
    response = requests.get(api_url)
    # Comprueba si la petición fue bien
    if response.status_code == 200:
        data = response.json()
        # Formatear los datos (esto dependerá de la estructura de la respuesta de la API)
        formatted_data = [{'id': item['id'], 'title': item['title']} for item in data]
        return JsonResponse({'data': formatted_data})
    else:
        return JsonResponse({'error': 'Unable to fetch data from external API'}, status=500)

#### `myproject/urls.py`

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]

#### `myapp/urls.py`

from django.urls import path
from .views import fetch_data

urlpatterns = [
    path('fetch-data/', fetch_data, name='fetch_data'),
]

#### `myapp/views.py`

import requests
from django.http import JsonResponse

def fetch_data(request):
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        formatted_data = [{'id': item['id'], 'title': item['title']} for item in data]
        return JsonResponse({'data': formatted_data})
    else:
        return JsonResponse({'error': 'Unable to fetch data from external API'}, status=500)

### Probar

    python manage.py runserver

    http://127.0.0.1:8000/myapp/fetch-data/