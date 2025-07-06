from django.shortcuts import render
from .models import Fotografia

def index(request):
    imagens = Fotografia.objects.all()
    
    return render(request, 'galeria/index.html', {'imagens':imagens})

def imagem(request, pk):
    imagem = Fotografia.objects.get(id=pk)
    return render(request, 'galeria/imagem.html')
