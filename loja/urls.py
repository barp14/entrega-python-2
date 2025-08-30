from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<int:id_produto>/', views.detalhe_produto, name="detalhe_produto"),
]
