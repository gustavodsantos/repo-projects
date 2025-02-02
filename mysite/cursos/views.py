from django.shortcuts import render

from mysite.cursos import facade


def indice(request):
    ctx = {'cursos': facade.listar_cursos_ordenados()}
    return render(request, 'cursos/indice.html', ctx)


def detalhe(request, slug):
    curso = facade.encontrar_curso(slug)
    return render(request, 'cursos/curso_detalhe.html', {'curso': curso})
