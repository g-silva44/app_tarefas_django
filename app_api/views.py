from django.shortcuts import render


# Create your views here.
def pessoa_perfil(request):
    return render(request, 'api/pessoa_perfil.html', context={})
