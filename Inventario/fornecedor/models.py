from django.db import models


class Fornecedor(models.Model):
    nome_fornecedor = models.CharField('Fornecedor', max_length=50)
    telefone_fornecedor = models.CharField(
        'Telefone', max_length=50, blank=True)

    def __str__(self):
        return self.nome_fornecedor
