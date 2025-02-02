from django.urls import path

from mysite.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('logged_out/', views.logged_out, name='logged_out'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
]
