from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel


class Curso(OrderedModel):
    titulo = models.CharField(max_length=64)
    descricao = models.TextField(null=True)
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('cursos:detalhe', kwargs={'slug': self.slug})
