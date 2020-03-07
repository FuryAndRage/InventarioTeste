from django import forms
from . models import BaixaProduto
from django.contrib.auth.models import User
from django.forms.widgets import HiddenInput

class BaixaProdutoForm(forms.ModelForm):
	
	class Meta:

		model = BaixaProduto
		fields = '__all__'
		widgets = {'user':forms.HiddenInput()}

