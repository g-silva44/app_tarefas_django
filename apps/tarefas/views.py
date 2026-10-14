from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.utils import timezone

from .forms import TarefaForm
from .models import TarefaModel


# Create your views here.

def index_view(request):
    username = request.user.username
    ultimas_tarefas = TarefaModel.objects.order_by('-data_criacao')[:3]
    tarefas_atrasadas = TarefaModel.objects.filter(
        completo=False,
        data_expiracao__lt=timezone.now(),
    )

    return render(request, 'index.html',
                  {'username': username, 'ultimas_tarefas': ultimas_tarefas, 'atrasadas': tarefas_atrasadas})


def tarefas_adicionar(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_home')
    context = {

        'form': TarefaForm()
    }

    return render(request, 'tarefas/adicionar.html', context)


def tarefas_home(request):
    tarefas = TarefaModel.objects.order_by('-data_criacao', '-pk')
    paginator = Paginator(tarefas, 9)

    page_obj = paginator.get_page(request.GET.get('page'))

    context = {
        'nome': request.user.username,
        'tarefas': page_obj,
        'page_obj': page_obj,
    }

    return render(request, 'tarefas/home.html', context)


def tarefas_concluir(request, id):
    tarefa = TarefaModel.objects.get(id=id)
    tarefa.completo = True
    tarefa.save()
    return redirect('tarefas_home')


def tarefas_reabrir(request, id):
    tarefa = TarefaModel.objects.get(id=id)
    tarefa.completo = False
    tarefa.save()
    return redirect('tarefas_home')


def tarefas_editar(request, id):
    tarefa = TarefaModel.objects.get(id=id)
    if request.method == 'GET':
        form = TarefaForm(instance=tarefa)
        return render(request, 'tarefas/adicionar.html', {'form': form})

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
    return redirect('tarefas_home')
