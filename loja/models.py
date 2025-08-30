from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    sessao_id = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f"Carrinho {self.id}"
    
    @property
    def total(self):
        return sum(item.subtotal for item in self.itemcarrinho_set.all())

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
    
    @property
    def subtotal(self):
        return self.quantidade * self.produto.preco