from django.contrib import admin
from .models import *
# Register your models here.

class detCategoria(admin.ModelAdmin):
    list_display = ('id','nomeCategoria')
    list_display_links = ('id','nomeCategoria')
    search_fields= ('nomeCategoria')
    list_per_page = ('0')
admin.site.register(Categoria,detCategoria)
