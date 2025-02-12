import pytest
from django.urls import reverse

from mysite.quiz.models import Aluno


@pytest.mark.django_db
def test_home_post_new_user(client):
    url = reverse('quiz:quiz')
    data = {'nome': 'Novo Usuário'}

    response = client.post(url, data)

    aluno = Aluno.objects.filter(nome='Novo Usuário').first()
    assert aluno is not None
    assert response.status_code == 302
    assert response.url == '/quiz/perguntas/1'


@pytest.mark.django_db
def test_home_post_existing_user(client):
    aluno = Aluno.objects.create(nome='Usuário Existente')
    url = reverse('quiz:quiz')
    data = {'nome': aluno.nome}

    response = client.post(url, data)

    assert response.status_code == 302
    assert response.url == '/quiz/perguntas/1'
    assert client.session['aluno_id'] == aluno.id
