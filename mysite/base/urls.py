from django.urls import path

from mysite.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('senhas/', views.gerador_senha, name='gerador_senha'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]
