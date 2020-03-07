from .models import Produto
from django.contrib import messages
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Sum, Q, Count, Case, When
from . forms import ProdutoForm

class ProdutoList(ListView):
    model = Produto
    template_name = 'p_list.html'
    context_object_name = 'produtos'
    paginate_by = 10
    ordering = '-id'
   

def NovoProduto(request):
    form = ProdutoForm()
    if request.method =='POST':
        form = ProdutoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            dados = Produto(
                nome_produto = form.cleaned_data['nome_produto'],
                quantidade_produto = form.cleaned_data['quantidade_produto'],
                descricao_produto = form.cleaned_data['descricao_produto'],
                compra_produto = form.cleaned_data['compra_produto'],
                venda_produto = form.cleaned_data['venda_produto'],
                foto_produto = form.cleaned_data['foto_produto']
                )
            dados.save()
            return redirect('produto:produto_lista')
        else:
            print('nao e valido')
    else:
        return render(request, 'produto_form.html',{'form':form})  


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = '__all__'
    success_url = reverse_lazy('produto:lista_produto')
    success_message = 'Produto Cadastrado com Sucesso'

    def form_valid(self, form):
        produto = form.save(commit = False)
        image = form.cleaned_data['foto_produto']
        user = self.request.user
        produto.save()

        return HttpResponseRedirect(self.success_url())