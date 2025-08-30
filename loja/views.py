from django.shortcuts import render, get_object_or_404
from .models import Produto

def lista_produtos(request):
    ultimo_produto = Produto.objects.order_by("-criado_em")[:5]
    context = {"ultimo_produto": ultimo_produto}
    return render(request, "loja/index.html", context)


def detalhe_produto(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    return render(request, "loja/detalhe.html", {"produto": produto})