from django.shortcuts import render, redirect
from .models import Imovel

# Create your views here.
def home(request):
  imoveis = Imovel.objects.all()
  return render(request, 'index.html', {'imoveis': imoveis})

def salvar(request):
  iptDescricao = request.POST.get('descricao')
  iptDataCompra = request.POST.get('dataCompra')
  iptEndereco = request.POST.get('endereco')
  Imovel.objects.create(descricao=iptDescricao, dataCompra=iptDataCompra, endereco=iptEndereco)
  imoveis = Imovel.objects.all()
  return render(request, 'index.html', {'imoveis': imoveis})

def editar(request, id):
  imovel = Imovel.objects.get(id=id)
  return render(request, 'update.html', {'imovel':imovel})

def update(request, id):
  iptDescricao = request.POST.get('descricao')
  iptDataCompra = request.POST.get('dataCompra')
  iptEndereco = request.POST.get('endereco')
  imovel = Imovel.objects.get(id=id)
  imovel.descricao = iptDescricao
  imovel.dataCompra = iptDataCompra
  imovel.endereco = iptEndereco
  imovel.save()
  return redirect(home)

def delete(request, id):
  imovel = Imovel.objects.get(id=id)
  imovel.delete()
  return redirect(home)

def salvarComodo(request,id):

  return redirect(home)

def deleteComodo(request, id):

  return redirect(home)