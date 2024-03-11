from django.contrib import admin
from .models import Condominio, Apartamento, Morador, Encomenda, Funcionario

# Register your models here.

class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone', 'email')
    search_fields = ('nome', 'endereco', 'telefone', 'email')
admin.site.register(Condominio, CondominioAdmin)

class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'condominio')
    search_fields = ('numero', 'condominio_nome')
admin.site.register(Apartamento, ApartamentoAdmin)

class MoradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apartamento', 'email', 'telefone')
    search_fields = ('nome', 'apartamento_numero', 'email', 'telefone')
admin.site.register(Morador, MoradorAdmin)

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','nomeF', 'condominio', 'funcaoFuncionario', 'email', 'telefone')
    search_fields = ('user', 'nomeF', 'condominio_nome', 'funcaoFuncionario', 'email', 'telefone')
admin.site.register(Funcionario, FuncionarioAdmin)

class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('morador', 'descricao', 'data_hora_recebimento', 'data_hora_entrega')
    search_fields = ('morador', 'descricao', 'data_hora_recebimento', 'data_hora_entrega')
admin.site.register(Encomenda, EncomendaAdmin)