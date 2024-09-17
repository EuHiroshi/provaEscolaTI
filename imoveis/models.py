from django.db import models

# Create your models here.
class Imovel(models.Model):
  descricao = models.CharField(max_length=100)
  dataCompra = models.DateField()
  endereco = models.CharField(max_length=100)

  def __str__(self):
    return self.descricao