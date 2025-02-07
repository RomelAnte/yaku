from django.shortcuts import render
from .models import Socio

# Create your views here.
def listadoSocios(request):
    socios = Socio.objects.all()
    return render(request, 'index.html', {'socios': socios})