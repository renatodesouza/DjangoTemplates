from django.contrib import admin

from .models import Fotografia


@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'descricao', 'foto')

    fieldsets = [
        ('Informações:',    {'fields':('nome', 'legenda', 'descricao', 'foto')})
    ]

    search_fields = ['nome']