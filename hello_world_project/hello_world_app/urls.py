from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('members/', views.all_members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/update/<slug:slug>/', views.update_member, name='update_member'),
    path('members/delete/<slug:slug>/', views.delete_member, name='delete_member'),
    path('testing/', views.testing, name='testing'), 
    path('testing/pagina/', views.pagina, name='pagina'),
]

# Quitamos la url details/id de urlpatterns
# path('members/details/<int:member_id>/', views.member, name='member'),