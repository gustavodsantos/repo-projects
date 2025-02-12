from django.urls import path

from mysite.quiz import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('perguntas/<int:indice>', views.perguntas, name='perguntas'),
    path('classificacao', views.classificacao, name='classificacao'),
]
