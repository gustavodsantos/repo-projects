from django.core.exceptions import ValidationError
from django.db import models


class Tarefa(models.Model):
    nome = models.CharField(max_length=255)
    feita = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    def clean(self):
        # Validações adicionais
        if not self.nome.strip():
            raise ValidationError('O campo nome não pode ser apenas espaços.')

    def save(self, *args, **kwargs):
        # Garante validação antes de salvar
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
