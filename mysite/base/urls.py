from django.urls import path

from mysite.base import views

app_name = 'base'

urlpatterns = [
    path('', views.sobre_min, name='sobre_min'),  # Página inicial
    path('senhas/', views.gerador_senha, name='gerador_senha'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]
