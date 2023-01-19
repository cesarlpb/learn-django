from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
        # app "polls" -> pregunta 5
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
        # app "polls" -> pregunta 5 -> resultados de pregunta 5
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
        # app "polls" -> pregunta 5 -> votar pregunta 5
    path('<int:question_id>/vote/', views.vote, name='vote'),
]