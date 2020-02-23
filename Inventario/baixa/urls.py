from django.urls import path
from . import views

app_name='baixa'
urlpatterns = [
	path('log/', views.log_baixa, name='log_baixa'),
	path('<int:pk>/produto/', views.baixa_produto, name='baixa_produto')
]