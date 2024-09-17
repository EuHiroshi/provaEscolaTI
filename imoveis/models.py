from django.db import models

# Create your models here.
class Imovel(models.Model):
  descricao = models.CharField(max_length=100)
  dataCompra = models.DateField()
  endereco = models.CharField(max_length=100)

  def __str__(self):
    return self.descricao

class Comodo(models.Model):
  nome = models.CharField(max_length=100)
  imovel = models.ForeignKey('Imovel', on_delete=models.CASCADE, related_name='comodos')

  def __str__(self):
      return self.nome