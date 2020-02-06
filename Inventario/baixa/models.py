from django.db import models
from Inventario.produto.models import Produto
from django.utils import timezone

class BaixaProduto(models.Model):
	baixa_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
	baixa_quantidade = models.IntegerField(verbose_name='Quantidade')
	baixa_motivo = models.TextField(verbose_name='Motivo')
	baixa_data = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.baixa_produto