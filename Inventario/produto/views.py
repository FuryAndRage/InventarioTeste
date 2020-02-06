from .models import Produto
from django.contrib import messages
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Sum, Q, Count, Case, When


class ProdutoList(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 10
    ordering = '-id'


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = '__all__'
    success_url = reverse_lazy('produto:lista_produto')
    success_message = 'Produto Cadastrado com Sucesso'
