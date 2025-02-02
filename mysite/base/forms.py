from django import forms
from django.contrib.auth.forms import UserCreationForm

from mysite.base.models import User


class RegistroUsuarioForm(UserCreationForm):
    """Formulário para cadastro de usuários"""

    nome = forms.CharField(max_length=64, label='Nome')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'nome']

    def save(self, commit=True):
        user = super().save(commit=False)
        nome = self.cleaned_data['nome']

        user.first_name = nome
        if commit:
            user.save()
        return user
