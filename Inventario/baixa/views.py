from django.shortcuts import render, redirect, get_object_or_404
from Inventario.produto.models import Produto
from .forms import BaixaProdutoForm
from . models import BaixaProduto
from django.contrib.auth.models import User
from django.contrib import messages
def log_baixa(request):
	template_name = 'log_baixa.html'
	log = BaixaProduto.objects.all()
	return render(request, template_name, {'log':log})


def baixa_produto(request, pk):
	prod = get_object_or_404(Produto, pk=pk)
	form = BaixaProdutoForm()
	
	if request.method == 'POST':
		form = BaixaProdutoForm(request.POST, instance=prod)
		baixa = request.POST.get('baixa_quantidade')
		if not baixa:
			baixa = 0
		qty = prod.quantidade_produto
		if form.is_valid():
			dados = BaixaProduto(
				user = request.user,
				baixa_produto = form.cleaned_data['baixa_produto'],
				baixa_quantidade = form.cleaned_data['baixa_quantidade'],
				baixa_motivo = form.cleaned_data['baixa_motivo'],
				baixa_data = form.cleaned_data['baixa_data']
				) 
			if int(baixa) > qty:
				messages.error(request, 'O quantidade a dar baixa e superior a quantidade em estoque')
				return redirect('produto:lista_produto')
			prod.quantidade_produto= qty - int(baixa)
			prod.save()
			dados.save()
			return redirect('produto:lista_produto')
	else:
		return render(request, 'baixa_form.html', {'form':form, 'prod':prod})