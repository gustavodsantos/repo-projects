from django.core.exceptions import ValidationError
from django.forms import ModelForm

from mysite.tarefas.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'feita']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.strip() == '':
            raise ValidationError('O nome da tarefa não pode ser vazio ou só conter espaços.')
        return nome
