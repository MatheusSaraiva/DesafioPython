from django.contrib import admin
from carros.models import Automovel, Marca


class Automoveis(admin.ModelAdmin):
    list_display = ('id', 'nome', 'km_por_galao', 'cilindros', 'cavalor_de_forca', 'peso', 'aceleracao', 'ano', 'origem', 'marca')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'origem')
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Automovel, Automoveis)

class Marcas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'origem')
    search_fields = ('nome', 'origem')
    list_per_page = 10
    ordering = ('nome',)

admin.site.register(Marca, Marcas)