from django.shortcuts import render, get_object_or_404, redirect
from .models import EntradaProduto
from .forms import EntradaProdutoForm
from Inventario.produto.models import Produto
from django.contrib.auth.models import User
from django.contrib import messages

def log_entrada(request):
	log = EntradaProduto.objects.all()
	return render(request, 'entrada_log.html', {'log':log})

def entrada_produto(request, pk):
	prod = get_object_or_404(Produto, pk = pk)
	form = EntradaProdutoForm()
	if request.method == 'POST':
		form = EntradaProdutoForm(request.POST or None, request.FILES or None)
		entrada = request.POST.get('entrada_quantidade')
		if not entrada:
			entrada = 0
		qty = prod.quantidade_produto
		if form.is_valid():
			dados =EntradaProduto(
				user = request.user,
				entrada_produto = form.cleaned_data['entrada_produto'],
				entrada_quantidade = form.cleaned_data['entrada_quantidade'],
				entrada_motivo = form.cleaned_data['entrada_motivo'],
				entrada_data = form.cleaned_data['entrada_data']
				) 
			if int(entrada) <= 0:
				messages.error(request, 'A quantidade de entrada tem que ser maior que 1')
				return redirect('produto:lista_produto')
			prod.quantidade_produto = qty + int(entrada)
			prod.save()
			form.save()
			return redirect('produto:lista_produto')
	else:
		return render(request, 'entrada_form.html', {'prod':prod, 'form':form})
