from django.contrib import admin
from django.urls import path
from A_Inicio.views import index

urlpatterns = [
    path("", index, name="index"),
]
