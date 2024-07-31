from django.contrib import admin
from django.urls import path, include
from myapp.views import index 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('myapp.urls')),
    path('', index, name='index'),  # Configurar la URL principal
]