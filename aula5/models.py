from django.db import models

# Create your models here.

class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    twitter = models.URLField()
    data = models.DateField()


    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        total = self.produto_set.all().aggregate(models.Sum('preco'))
        return total["preco__sum"]

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
