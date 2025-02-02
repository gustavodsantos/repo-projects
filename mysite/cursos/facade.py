from typing import List

from mysite.cursos.models import Curso


def listar_cursos_ordenados() -> List[Curso]:
    """
    Lista cursos ordenados por parâmetro order
    :return:
    """

    return list(Curso.objects.order_by('order').all())


def encontrar_curso(slug: str) -> Curso:
    return Curso.objects.get(slug=slug)
