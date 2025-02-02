from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from mysite.cursos.models import Curso


@admin.register(Curso)
class CursoAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'slug', 'descricao', 'order', 'move_up_down_links')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo', 'descricao')
    list_filter = ('titulo',)
    ordering = ['order', 'titulo']
