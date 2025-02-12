from django.urls import path

from mysite.tarefas import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.tarefas, name='tarefas'),
    path('tarefa/<int:tarefa_id>/feita/', views.marcar_como_feita, name='marcar_como_feita'),
    path('tarefa/<int:tarefa_id>/pendente/', views.marcar_como_pendente, name='marcar_como_pendente'),
    path('tarefa/<int:tarefa_id>/apagar/', views.apagar_tarefa, name='apagar_tarefa'),
]
