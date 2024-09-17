from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete, verComodos, salvarComodo, deleteComodo

urlpatterns = [
    path('', home, name='home'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('verComodos/<int:id>', verComodos, name='verComodos'),
    path('salvarComodo/<int:id>', salvarComodo, name='salvarComodo'),
    path('deleteComodo/<int:imovel_id>/<int:comodo_id>', deleteComodo, name='deleteComodo'),
]

