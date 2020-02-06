from django.urls import path
from . import views
app_name = 'produto'
urlpatterns = [
    path('lista/', views.ProdutoList.as_view(), name='lista_produto'),
    path('novo/', views.ProdutoCreate.as_view(), name='novo_produto')
]
