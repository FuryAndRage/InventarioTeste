from django.contrib import admin
from .models import EntradaProduto

@admin.register(EntradaProduto)
class EntradaProdutoAdmin(admin.ModelAdmin):
	list_display = ('entrada_data','entrada_produto','entrada_quantidade',)
	search_fields = ('entrada_data','entrada_produto')
# Register your models here.
