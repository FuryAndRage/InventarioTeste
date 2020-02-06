from django.contrib import admin
from .models import BaixaProduto

@admin.register(BaixaProduto)
class BaixaProdutoAdmin(admin.ModelAdmin):
	list_display = ('baixa_data','baixa_produto','baixa_quantidade',)
	search_display = ('baixa_produto', 'baixa_quantidade',)
