from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:pk>/', views.imagem, name='imagem')
]