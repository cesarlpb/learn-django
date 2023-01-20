from django.urls import path

#from . import views # importa todas las vistas y hay que navegar como "views.MyView.as_view()"
#from class_views.views import MyView # importa solo la vista que necesitamos y navegamos como "MyView.as_view()"
from class_views.views import SubClaseView

# Ejemplo con animales y perros y gatos
from class_views.views import Perro, Gato, CreateAnimalFormView, SuccessView, ErrorView, AnimalListView
from class_views.views import PublisherListView

app_name = 'class_views'
urlpatterns = [
    path('', SubClaseView.as_view(), name='index'),
    path('success/', SuccessView.as_view(), name='success'),
    path('error/', ErrorView.as_view(), name='error'),
    path('animal/', AnimalListView.as_view(), name='animal'),                                     
    path('animal/create/', CreateAnimalFormView.as_view(), name='create_animal'),
    path('animal/perro/', Perro.as_view(), name='perro'),
    path('animal/gato/', Gato.as_view(), name='gato'),
    path('publishers/', PublisherListView.as_view()),
]
"""
 path('', views.IndexView.as_view(), name='index')
path('<int:pk>/', views.DetailView.as_view(), name='detail'),
path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
"""