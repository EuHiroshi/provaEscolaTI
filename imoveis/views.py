from django.shortcuts import render, redirect
from .models import Imovel, Comodo

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

def verComodos(request, id):
  imovel = Imovel.objects.get(id=id)
  comodos = Comodo.objects.filter(imovel=imovel)
  return render(request, 'comodo.html', {'imovel':imovel, 'comodos': comodos})

def salvarComodo(request, id):
  imovel = Imovel.objects.get(id=id)
  nome_comodo = request.POST.get('nome_comodo')
  Comodo.objects.create(nome=nome_comodo, imovel=imovel)
  comodos = Comodo.objects.filter(imovel=imovel)
  return render(request, 'comodo.html', {'imovel': imovel, 'comodos': comodos})

def deleteComodo(request, imovel_id, comodo_id):
  imovel = Imovel.objects.get(id=imovel_id)  
  comodo = Comodo.objects.get(id=comodo_id, imovel=imovel)  
  comodo.delete()
  comodos = Comodo.objects.filter(imovel=imovel)     
  return render(request, 'comodo.html', {'imovel': imovel, 'comodos': comodos})
