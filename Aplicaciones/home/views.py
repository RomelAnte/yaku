from django.shortcuts import render
from .utils import promedio_consumo, estado_lectura, total_consumo_mensual

# Create your views here.
def home(request):
    return render(request, 'index.html')

def dashboards(request):
    context = {
        'consumo_mensual': promedio_consumo(),
        'estado_lectura': estado_lectura(),
        'total_consumos': total_consumo_mensual()
    }
    return render(request, 'dashboards.html', context)