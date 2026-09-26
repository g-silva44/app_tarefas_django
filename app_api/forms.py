from django import forms
from .models import PessoaModel


class PessoaForm(forms.ModelForm):
    class Meta:
        ordering = ['nome']
        model = PessoaModel
        fields = ['nome', 'email', 'senha', 'telefone']


class PessoaLoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        ordering = ['nome']
        model = PessoaModel
        fields = ['email', 'senha']
