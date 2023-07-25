from django.shortcuts import render, redirect
from .models import Produto
from .form import ProdutoForm 

# Create your views here.


def home(request):
    dados = {}
    dados['produto'] = Produto.objects.all()
    return render(request, "home.html", dados)

def novo_produto(request):
    dados = {}
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    dados['form'] = form
    return render(request, 'form.html', dados)

def update(request, pk):
    dados = {}
    produto = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('url_home')
    dados['form'] = form
    return render(request, 'form.html', dados)

def delete(request, pk):
    produto = Produto.objects.get(pk=pk)
    produto.delete()
    return redirect("url_home")
