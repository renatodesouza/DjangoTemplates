from django.shortcuts import render
from models import Fotografia

def index(request):
    imagens = Fotografia.objects.all()
    
    return render(request, 'galeria/index.html', {'imagens':imagens})

def imagem(request):
    return render(request, 'galeria/imagem.html')
