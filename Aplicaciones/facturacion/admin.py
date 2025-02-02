from django.contrib import admin
from models import Consumo, Recaudacion, Impuesto, Detalle

# Register your models here.
admin.site.register(Consumo)
admin.site.register(Recaudacion)
admin.site.register(Impuesto)
admin.site.register(Detalle)