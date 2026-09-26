from django.urls import path

from app_api import views

urlpatterns = [
    path('perfil/', views.pessoa_perfil, name='pessoa_perfil'),
    path('perfil/registrar/', views.pessoa_registrar, name='pessoa_registrar'),
    path('perfil/entrar', views.pessoa_entrar, name='pessoa_entrar'),
    path('perfil/sair', views.pessoa_sair, name='pessoa_sair')
]
