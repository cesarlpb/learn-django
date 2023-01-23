from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('members/', views.all_members, name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/update/<slug:slug>/', views.update_member, name='update_member'),
    path('members/delete/<slug:slug>/', views.delete_member, name='delete_member'),
    path('modelo/', views.modelo, name="modelo"),
]

# Quitamos la url details/id de urlpatterns
# path('members/details/<int:member_id>/', views.member, name='member'),