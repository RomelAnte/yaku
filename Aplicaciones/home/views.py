from django.shortcuts import render
from .utils import promedio_consumo, estado_lectura, total_consumo_mensual, total_eventos_tipo, total_socios_tipo
from .utils import porcentaje_medidores_uso, total_asistente_eventos

# Create your views here.
def home(request):
    return render(request, 'index.html')

def dashboards(request):
    context = {
        'consumo_mensual': promedio_consumo(),
        'estado_lectura': estado_lectura(),
        'total_consumos': total_consumo_mensual(),
        'total_eventos_tipo' : total_eventos_tipo(),
        'total_socios_tipo' : total_socios_tipo(),
        'porcentaje_medidores_uso' : porcentaje_medidores_uso(),
        'total_asistente_eventos': total_asistente_eventos,
    }
    return render(request, 'dashboards.html', context)