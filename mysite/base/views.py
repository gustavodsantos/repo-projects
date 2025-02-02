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


def home(request):
    return render(request, 'base/home.html')
