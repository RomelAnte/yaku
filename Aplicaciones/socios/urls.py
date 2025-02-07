from django.urls import path
from . import views

app_name = 'socios'

urlpatterns = [
    path('', views.listadoSocios, name='listadoSocios'),
]