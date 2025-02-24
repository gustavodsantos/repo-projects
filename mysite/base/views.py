import random
import string

from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mysite.base.forms import RegistroUsuarioForm


def logged_out(request):
    return render(request, 'registration/logged_out.html')


# View para registrar um novo usuário
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após registro
            messages.success(request, 'Cadastro realizado com sucesso!')
            return HttpResponseRedirect(reverse('base:home'))
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registrar_usuario.html', {'form': form})


def sobre_min(request):
    return render(request, 'base/sobre_min.html')


def gerador_senha(request):
    # Define os critérios padrão
    comprimento = int(request.GET.get('length', 12))  # Comprimento padrão
    caracteres = string.ascii_lowercase  # Letras minúsculas

    if request.GET.get('uppercase'):
        caracteres += string.ascii_uppercase
    if request.GET.get('numbers'):
        caracteres += string.digits
    if request.GET.get('special'):
        caracteres += string.punctuation

    # Gerar senha
    senha = ''.join(random.choices(caracteres, k=comprimento))

    return render(request, 'base/gerador_senha.html', {'senha': senha})
