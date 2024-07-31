from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_factura, name='crear_factura'),
    path('agregar_productos/<int:factura_id>/', views.agregar_productos, name='agregar_productos'),
    path('detalle/<int:factura_id>/', views.detalle_factura, name='detalle_factura'),
]