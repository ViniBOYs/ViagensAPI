from django.contrib import admin
from .models import *
# Register your models here.

class detCategoria(admin.ModelAdmin):
    list_display = ('id','nomeCategoria')
    list_display_links = ('id','nomeCategoria')
    search_fields= ('nomeCategoria')
    list_per_page = (10)
admin.site.register(Categoria,detCategoria)

class detLocal(admin.ModelAdmin):
    list_display = ('id','nomeLocal','cidade')
    list_display_links = ('id','nomeLocal')
    search_fields= ('id')
    list_per_page = (10)
admin.site.register(Local,detLocal)

class detPeriodo(admin.ModelAdmin):
    list_display = ('id','inicioPeriodo','finalPeriodo')
    list_display_links = ('id')
    search_fields= ('id')
    list_per_page = (10)
admin.site.register(Periodo,detPeriodo)

class detViagem(admin.ModelAdmin):
    list_display = ('id','titulo','valorDiaria','animal','periodoFK','periodoDias','categoriaFK')
    list_display_links = ('id','titulo')
    search_fields= ('id')
    list_per_page = (10)
admin.site.register(Viagem,detViagem)