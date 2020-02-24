from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'produto'
urlpatterns = [
    path('lista/', views.ProdutoList.as_view(), name='lista_produto'),
    path('novo/', views.ProdutoCreate.as_view(), name='novo_produto')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
