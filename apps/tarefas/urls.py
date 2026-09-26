from django.urls import path

from . import views

urlpatterns = [
    path('', views.tarefas_home, name='tarefas_home'),
    path('adicionar/', views.tarefas_adicionar, name='tarefas_adicionar'),
    path('concluir/<int:id>/', views.tarefas_concluir, name='tarefas_concluir'),
    path('reabrir/<int:id>/', views.tarefas_reabrir, name='tarefas_reabrir'),
    path('editar/<int:id>/', views.tarefas_editar, name='tarefas_editar')
]
