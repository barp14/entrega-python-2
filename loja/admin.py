from django.contrib import admin

# Register your models here.

from .models import Categoria, Produto, Carrinho, ItemCarrinho

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)
