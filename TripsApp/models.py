from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    nomeCategoria = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nomeCategoria
    

class Local(models.Model):
    nomeLocal = models.CharField(max_length=100, null=False)
    descBreve = models.CharField(max_length=125, null=False)
    endereco = models.CharField(max_length=150, null=False)
    cidade = models.CharField(max_length=50, null=False)
    categoriaFK = models.ForeignKey(Categoria, related_name='categoriaFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomeLocal

class Periodo(models.Model):
    inicioPeriodo = models.DateField(auto_now_add=True)
    finalPeriodo = models.DateField(auto_now_add=True)
    diasPeriodo = abs((finalPeriodo - inicioPeriodo).days)
    
    def __str__(self):
        return self.inicioPeriodo

class Viagem(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=200, null=False)
    valorDiaria = models.DecimalField(max_digits=6, decimal_places=2)
    animal = models.BooleanField(null=False)
    periodoFK = models.ForeignKey(Periodo, related_name='periodoFK', on_delete=models.CASCADE)
    periodoDias = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.periodoDias = self.periodoFK.diasPeriodo
        super(Viagem, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    

class Foto(models.Model):
    imagem = models.CharField(max_length=300, null=False)
    viagemFK = models.ForeignKey(Viagem, related_name='viagemFK', on_delete=models.CASCADE)
    localFK = models.ForeignKey(Local, related_name='localFK', on_delete=models.CASCADE)

    def __str__(self):
        return self.imagem


class TipoPagamento(models.Model):
    nomePagamento = models.CharField(max_length=50, null= False)
    descricao = models.CharField(max_length=300, null= False)
    
    def __str__(self):
        return self.nomePagamento


class Pagamento(models.Model):
    user_fk = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    viagemFK =  models.ForeignKey(Viagem, related_name='viagemFK', on_delete=models.CASCADE)
    modoPagamento = models.ForeignKey(TipoPagamento,related_name='modoPagamento',on_delete=models.CASCADE)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    animal = models.IntegerField(default=0)
    qtdPessoas = models.IntegerField(default=1)
    
    def save(self, *args, **kwargs):
        self.valorTotal = self.viagemFK.periodoDias * self.viagemFK.valorDiaria * (self.animal/3) * self.qtdPessoas
        super(Pagamento, self).save(*args, **kwargs)

    def __str__(self):
        return self.modoPagamento


class Reserva(models.Model):
    pagamentoFK = models.ForeignKey(Pagamento, related_name='pagamentoFK', on_delete=models.CASCADE)
    viagemFK = models.ForeignKey(Viagem, related_name='viagemFK',on_delete=models.CASCADE)
    qtdPessoas = models.IntegerField(default=1)
    valorFinal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    animal = models.BooleanField()

    def save(self, *args, **kwargs):
        self.qtdPessoas = self.pagamentoFK.qtdPessoas
        self.valorFinal = self.pagamentoFK.valorTotal
        self.animal = self.pagamentoFK.animal         
        super(Pagamento, self).save(*args, **kwargs)


    def __str__(self):
        return self.valorFinal




    







'''
class x(models.Model):

    def __str__(self):
        return self.
'''