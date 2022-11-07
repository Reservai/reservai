from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Restaurantes

def index(request):
    restaurantes = Restaurantes.objects.all

    dados = {
        'restaurantes' : restaurantes
    }

    return render(request,'index.html',dados)