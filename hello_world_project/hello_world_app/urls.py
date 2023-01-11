from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello_world, name='hello_world'),
    path('members/', views.all_members, name='members'),
]