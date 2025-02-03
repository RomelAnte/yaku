from django.contrib import admin
from .models import Medidor, Lectura

# Register your models here.
admin.site.register(Medidor)
admin.site.register(Lectura)