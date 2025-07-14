from django.contrib import admin
from .models import Usuario, Piscina, Monitoramento

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nome_completo', 'tipo')

@admin.register(Piscina)
class PiscinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao')

@admin.register(Monitoramento)
class MonitoramentoAdmin(admin.ModelAdmin):
    list_display = ('piscina', 'ph', 'temperatura', 'data_medicao')
