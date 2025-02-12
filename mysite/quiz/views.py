import random

from django.contrib import messages
from django.shortcuts import redirect, render

from mysite.quiz.forms import AlunoForm
from mysite.quiz.models import Aluno, Partida, Pergunta, Resposta


def quiz(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        try:
            aluno = Aluno.objects.get(nome=nome)
        except Aluno.DoesNotExist:
            form = AlunoForm(request.POST)
            if form.is_valid():
                aluno = form.save()
                request.session['aluno_id'] = aluno.id
            else:
                return render(request, 'quiz/quiz.html', {'form': form})

        request.session['aluno_id'] = aluno.id

        # Criar uma nova partida para o aluno
        partida = Partida.objects.create(aluno=aluno)
        request.session['partida_id'] = partida.id

        # Selecionar perguntas para a partida
        try:
            perguntas = selecionar_perguntas()
            request.session['perguntas_ids'] = [p.id for p in perguntas]
        except ValueError as e:
            messages.error(request, str(e))
            return redirect('quiz:quiz')

        # Redirecionar para a primeira pergunta
        return redirect('/quiz/perguntas/1')

    return render(request, 'quiz/quiz.html', {'form': AlunoForm()})


def perguntas(request, indice: int):
    aluno_id = request.session.get('aluno_id')
    partida_id = request.session.get('partida_id')
    perguntas_ids = request.session.get('perguntas_ids', [])

    if not aluno_id or not partida_id or not perguntas_ids:
        return redirect('quiz:quiz')

    aluno = Aluno.objects.filter(id=aluno_id).first()
    partida = Partida.objects.filter(id=partida_id, finalizada=False).first()

    if not aluno or not partida:
        return redirect('quiz:quiz')

    try:
        pergunta_id = perguntas_ids[indice - 1]
        pergunta = Pergunta.objects.get(id=pergunta_id)
    except (IndexError, Pergunta.DoesNotExist):
        partida.finalizada = True
        partida.save()
        return redirect('quiz:classificacao')

    if request.method == 'POST':
        resposta_indice = int(request.POST.get('resposta_indice', -1))

        # Adiciona a verificação de resposta duplicada para esta pergunta
        try:
            _, pontos = Resposta.registrar_resposta(aluno, pergunta, partida, resposta_indice)
            messages.success(request, f'Você ganhou {pontos} pontos!')
        except Exception:
            # Exibe mensagem de erro caso tente violar a unicidade
            messages.error(request, 'Erro ao registrar a resposta. Você já respondeu a essa pergunta.')

        # Redireciona para a próxima pergunta
        return redirect(f'/quiz/perguntas/{indice + 1}')

    return render(
        request,
        'quiz/perguntas.html',
        {
            'indice_da_questao': indice,
            'pergunta': pergunta,
            'aluno_nome': aluno.nome,
        },
    )


def classificacao(request):
    aluno_id = request.session.get('aluno_id')
    if not aluno_id:
        return redirect('quiz:quiz')

    aluno = Aluno.objects.get(id=aluno_id)

    # Atualizar pontuação total do aluno (se necessário)
    aluno.atualizar_pontuacao_maxima()

    # Obter todos os alunos ordenados por pontuação máxima
    ranking_completo = Aluno.objects.order_by('-pontuacao_maxima')

    # Calcular a posição do aluno no ranking
    posicao = None
    for indice, aluno_atual in enumerate(ranking_completo, start=1):
        if aluno_atual.id == aluno.id:
            posicao = indice
            break

    # Obter os 10 melhores para exibição no ranking
    melhores_alunos = ranking_completo[:10]

    context = {
        'pontos': aluno.pontuacao_maxima,
        'posicao': posicao,
        'primeiros_alunos_do_ranking': melhores_alunos,
    }

    return render(request, 'quiz/classificacao.html', context)


def selecionar_perguntas():
    perguntas = {
        'facil': Pergunta.objects.filter(dificuldade='facil', disponivel=True),
        'medio': Pergunta.objects.filter(dificuldade='medio', disponivel=True),
        'dificil': Pergunta.objects.filter(dificuldade='dificil', disponivel=True),
        'especialista': Pergunta.objects.filter(dificuldade='especialista', disponivel=True),
    }

    selecionadas = []
    try:
        # Seleciona questões de cada nível
        selecionadas.extend(random.sample(list(perguntas['facil']), min(2, perguntas['facil'].count())))
        selecionadas.extend(random.sample(list(perguntas['medio']), min(2, perguntas['medio'].count())))
        selecionadas.extend(random.sample(list(perguntas['dificil']), min(3, perguntas['dificil'].count())))
        selecionadas.extend(random.sample(list(perguntas['especialista']), min(3, perguntas['especialista'].count())))
    except ValueError:
        raise ValueError('Não há perguntas suficientes disponíveis em um ou mais níveis de dificuldade.')

    # Embaralha a lista de perguntas antes de retornar
    random.shuffle(selecionadas)
    return selecionadas
