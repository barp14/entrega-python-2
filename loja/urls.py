from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<int:id_produto>/', views.detalhe_produto, name="detalhe_produto"),
    path('carrinho/', views.ver_carrinho, name="ver_carrinho"),
    path('adicionar-ao-carrinho/<int:id_produto>/', views.adicionar_ao_carrinho, name="adicionar_ao_carrinho"),
    path('remover-do-carrinho/<int:item_id>/', views.remover_do_carrinho, name="remover_do_carrinho"),
    path('atualizar-carrinho/<int:item_id>/', views.atualizar_carrinho, name="atualizar_carrinho"),
]