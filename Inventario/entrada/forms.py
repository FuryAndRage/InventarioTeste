from django import forms
from .models import EntradaProduto
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput


class EntradaProdutoForm(forms.ModelForm):
	class Meta:
		model = EntradaProduto
		fields = '__all__'
