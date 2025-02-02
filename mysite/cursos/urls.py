from django.urls import path

from mysite.cursos import views

app_name = 'cursos'
urlpatterns = [
    path('<slug:slug>/', views.detalhe, name='detalhe'),
    path('', views.indice, name='indice'),
]
