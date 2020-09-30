from django.db import models

# Create your models here.

# Quero Persistir Dados


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self): # Forma de representar o objeto. Posso retornar um de seus atributos
        # ou retornar o que quiser.
        #return self.nome
        return f"{self.nome} - Numero em estoque: {self.estoque}"


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'