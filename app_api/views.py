from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app_api.forms import PessoaForm, PessoaLoginForm


@login_required
def pessoa_perfil(request):
    return render(request, 'api/pessoa_perfil.html', {'user': request.user})


def pessoa_registrar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa_perfil')

    context = {
        'form': PessoaForm()
    }
    return render(request, 'api/pessoa_registrar.html', context)


def pessoa_entrar(request):
    if request.method == 'POST':
        form = PessoaLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['senha'])
            if user:
                login(request, user)
                redirect('pessoa_perfil')
        else:
            raise Exception('Erro ao logar')

    context = {
        'form': PessoaLoginForm()
    }
    return render(request, 'api/pessoa_entrar.html', context)


@login_required
def pessoa_sair(request):
    return redirect('index')
