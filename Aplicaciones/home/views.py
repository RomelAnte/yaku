from django.shortcuts import render
from .utils import promedio_consumo

# Create your views here.
def home(request):
    return render(request, 'index.html')

def dashboards(request):
    context = {
        'consumo_mensual': promedio_consumo(),
    }
    return render(request, 'dashboards.html', context)