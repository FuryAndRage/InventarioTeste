from django.db import models
from django.db.models import Sum


class Produto(models.Model):
    nome_produto = models.CharField('Produto', max_length=100)
    quantidade_produto = models.IntegerField(verbose_name='Quantidade')
    descricao_produto = models.TextField(verbose_name='Descricao')
    compra_produto = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Preco Compra', null=True)
    venda_produto = models.DecimalField(
        verbose_name='Preco Venda', max_digits=5, decimal_places=2, null=True)

    @property
    def total_compra_produto(self):
        return self.objects.aggregate(total=Sum('compra_produto'))['total']

    @property
    def total_venda_produto(self):
        return self.objects.aggregate(total=Sum('venda_produto'))['total']

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome_produto
