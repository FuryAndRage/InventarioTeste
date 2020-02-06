from django.contrib import admin
from .models import Fornecedor


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome_fornecedor', 'telefone_fornecedor')
    search_fields = ('nome_fornecedor',)
