from django.contrib import admin
from django.urls import path
from A_Inicio.views import index, login

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
]
