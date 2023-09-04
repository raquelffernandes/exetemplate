from django.shortcuts import render
from django.http import HttpResponse
from .models import Amani,Carrossel,Imagens

# Create your views here.

def index(request):
    all_products = Amani.objects.all()
    all_sliders = Carrossel.objects.all()
    all_imagens = Imagens.objects.all()
    return render(request,'index.html',{"produto": all_products, "slider": all_sliders, "imagem": all_imagens})


def teste(request):
    all_entries = Amani.objects.all()
    retorno = all_entries
    return HttpResponse(retorno)
    