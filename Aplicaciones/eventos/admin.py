from django.contrib import admin
from .models import TipoEvento, Evento

# Register your models here.
admin.site.register(TipoEvento)
admin.site.register(Evento)