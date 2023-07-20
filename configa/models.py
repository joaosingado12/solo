from django.db import models

# Create your models here.

class Categoria(models.Model):
    nomeCategoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nomeCategoria

class Produto(models.Model):
    nomeProduto = models.CharField(max_length=50)
    descricaoProduto = models.CharField(max_length=200, null=True, blank=True)
    precoProduto = models.DecimalField(max_digits=4, decimal_places=2)
    categoriaProduto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomeProduto
    class Meta:
        verbose_name_plural = 'Produtos'
