from django.contrib import admin
from core.models import UnidadeFederativa, Cidade, Cinema, RegistroFilme
# Register your models here.

admin.site.register(UnidadeFederativa)
admin.site.register(Cidade)
admin.site.register(Cinema)
admin.site.register(RegistroFilme)