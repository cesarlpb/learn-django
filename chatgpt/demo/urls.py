from django.urls import path, include

from . import views

app_name = 'demo'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('demo/', include([
        path('', views.IndexView.as_view(), name='index'),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('new_query/', views.new_query, name='new_query'),
    ])),
]

"""
path('<int:pk>/', views.DetailView.as_view(), name='detail'),
path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
path('<int:question_id>/vote/', views.vote, name='vote'),
"""