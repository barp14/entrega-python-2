from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from loja import views 

def index(request):
    return HttpResponse("Index")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loja/', include('loja.urls')),
    path('', index),
]
    