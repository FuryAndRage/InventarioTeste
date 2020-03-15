from django.urls import path
from . import views

app_name = 'entrada'
urlpatterns = [
	path('log/', views.log_entrada, name='log_entrada'),
	path('<int:pk>/produto/', views.entrada_produto, name='entrada_produto'),
]