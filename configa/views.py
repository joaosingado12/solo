from django.shortcuts import render
from .models import Produto
from .form import ProdutoForm 

# Create your views here.


def home(request):
    dados = {}
    dados['produto'] = Produto.objects.all()
    return render(request, "home.html", dados)

def novo_produto(request):
    dados = {}
    form = ProdutoForm
    dados['form'] = form
    return render(request, 'create_new_product.html', dados)