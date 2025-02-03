from django.contrib import admin

from mysite.tarefas.models import Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'feita', 'criada_em', 'atualizada_em')
