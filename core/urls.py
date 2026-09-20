from django.contrib import admin
from django.urls import path, include

from apps.tarefas.views import *
from app_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('tarefas/', include('apps.tarefas.urls')),
    path('', include('app_api.urls')),
]
