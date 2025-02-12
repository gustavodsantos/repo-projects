from django.forms import ModelForm

from mysite.quiz.models import Aluno


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome']
