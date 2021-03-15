from django.contrib import admin
from aniversarios.models import Aniversario

class Aniversarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_aniversario')
    list_display_links = ('id', 'nome', 'data_aniversario')
    search_fields = ('nome', 'data_aniversario')
    list_per_page = 20

admin.site.register(Aniversario, Aniversarios)