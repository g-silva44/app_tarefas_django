from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import TarefaForm
from .models import TarefaModel


# Create your views here.

def index_view(request):
    return render(request, 'index.html')


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
    tarefas = TarefaModel.objects.all()
    paginator = Paginator(tarefas, 12)

    page_number = request.GET.get("page")
    paginas = paginator.get_page(page_number)
    context = {
        'nome': request.user.username,
        'tarefas': paginas
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
        form = TarefaForm(request.GET, instance=tarefa)
        return render(request, 'tarefas/adicionar.html', {'form': form})

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
    return redirect('tarefas_home')
