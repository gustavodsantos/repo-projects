from mysite.cursos import facade


def listar_cursos(request):
    return {'CURSOS': facade.listar_cursos_ordenados()}
