import pytest
from django.urls import reverse

# Importa as funções do módulo de views


@pytest.mark.django_db
def test_indice_view(client, monkeypatch):
    # Define um retorno fake para a função listar_cursos_ordenados
    fake_cursos = ['Curso A', 'Curso B']
    monkeypatch.setattr('mysite.cursos.facade.listar_cursos_ordenados', lambda: fake_cursos)

    # Obtenha a URL da view. Ajuste o nome se necessário.
    url = reverse('cursos:indice')
    response = client.get(url)

    # Verifica se a resposta é 200 (OK)
    assert response.status_code == 200

    # Verifica se o contexto contém a lista de cursos correta
    assert 'cursos' in response.context
    assert response.context['cursos'] == fake_cursos

    # Opcional: verifique se o template correto foi utilizado
    assert 'cursos/indice.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_detalhe_view(client, monkeypatch):
    # Define um curso fake que será retornado pela função encontrar_curso
    fake_curso = {
        'titulo': 'Curso Teste',
        'slug': 'curso-teste',
        # adicione outros campos se necessário
    }
    monkeypatch.setattr(
        'mysite.cursos.facade.encontrar_curso', lambda slug: fake_curso if slug == 'curso-teste' else None
    )

    # Obtenha a URL da view de detalhe.
    url = reverse('cursos:detalhe', kwargs={'slug': 'curso-teste'})
    response = client.get(url)

    # Verifica se a resposta é 200 (OK)
    assert response.status_code == 200

    # Verifica se o contexto contém o curso correto
    assert 'curso' in response.context
    assert response.context['curso'] == fake_curso

    # Opcional: verifique se o template correto foi utilizado
    assert 'cursos/curso_detalhe.html' in [t.name for t in response.templates]
