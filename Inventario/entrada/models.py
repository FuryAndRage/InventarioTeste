from django.db import models
from Inventario.produto.models import Produto
from django.utils import timezone
from django.contrib.auth.models import User

class EntradaProduto(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='User')
	entrada_produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produto')
	entrada_quantidade = models.IntegerField(verbose_name='Quantidade')
	entrada_motivo = models.TextField(null=True)
	entrada_data = models.DateTimeField(default=timezone.now)
	class Meta:
		verbose_name = "Entrada"
		verbose_name_plural = "Entradas"

	def __str__(self):
		return self.entrada_produto


