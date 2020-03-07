from django.urls import path
from . import views


app_name = 'produto'
urlpatterns = [
    path('lista/', views.ProdutoList.as_view(), name='lista_produto'),
    path('novo/', views.NovoProduto, name='novo_produto'),

]


