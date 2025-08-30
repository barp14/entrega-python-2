from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Carrinho, ItemCarrinho

def lista_produtos(request):
    ultimo_produto = Produto.objects.order_by("-criado_em")[:5]
    context = {"ultimo_produto": ultimo_produto}
    return render(request, "loja/index.html", context)


def detalhe_produto(request, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    return render(request, "loja/detalhe.html", {"produto": produto})


def obter_ou_criar_carrinho(request):
    if request.user.is_authenticated:
        # Usuário está logado, obter ou criar seu carrinho
        carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)
    else:
        # Usuário anônimo, usar ID de sessão
        chave_sessao = request.session.session_key
        if not chave_sessao:
            request.session.create()
            chave_sessao = request.session.session_key
        
        carrinho, criado = Carrinho.objects.get_or_create(sessao_id=chave_sessao)
    
    return carrinho

def adicionar_ao_carrinho(request, id_produto):
    if request.method == 'POST':
        produto = get_object_or_404(Produto, pk=id_produto)
        quantidade = int(request.POST.get('quantidade', 1))
        
        if quantidade <= 0:
            quantidade = 1
            
        if quantidade > produto.estoque:
            quantidade = produto.estoque
        
        carrinho = obter_ou_criar_carrinho(request)
        
        # Verificar se o item já está no carrinho
        item_carrinho, criado = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho,
            produto=produto,
            defaults={'quantidade': quantidade}
        )
        
        if not criado:
            # Atualizar quantidade se já estiver no carrinho
            item_carrinho.quantidade += quantidade
            if item_carrinho.quantidade > produto.estoque:
                item_carrinho.quantidade = produto.estoque
            item_carrinho.save()
            
        return redirect('ver_carrinho')
    
    return redirect('detalhe_produto', id_produto=id_produto)

def ver_carrinho(request):
    carrinho = obter_ou_criar_carrinho(request)
    itens = carrinho.itemcarrinho_set.all()
    
    context = {
        'itens': itens,
        'total': carrinho.total
    }
    
    return render(request, 'loja/carrinho.html', context)

def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, pk=item_id)
    item.delete()
    return redirect('ver_carrinho')

def atualizar_carrinho(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(ItemCarrinho, pk=item_id)
        quantidade = int(request.POST.get('quantidade', 1))
        
        if quantidade <= 0:
            # Remover o item se a quantidade for 0 ou menos
            item.delete()
        else:
            # Atualizar quantidade, limitada pelo estoque
            if quantidade > item.produto.estoque:
                quantidade = item.produto.estoque
            
            item.quantidade = quantidade
            item.save()
            
    return redirect('ver_carrinho')