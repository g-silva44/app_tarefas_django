from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import TarefaForm
from .models import TarefaModel

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def tarefas_adicionar (request: HttpRequest):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas_home')
    context = {

        'form': TarefaForm()
    }
    return render(request, 'tarefas/adicionar.html', context)

def tarefas_home (request):
    context = {
        'nome': 'João',
        'tarefas': TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', context)