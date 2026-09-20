from django.urls import path

from app_api import views

urlpatterns = [
    path('perfil/', views.pessoa_perfil, name='pessoa_perfil'),
]
