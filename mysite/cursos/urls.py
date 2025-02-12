from django.urls import path

from mysite.cursos import views

app_name = 'cursos'
urlpatterns = [
    path('', views.indice, name='indice'),
    path('<slug:slug>/', views.detalhe, name='detalhe'),
]
