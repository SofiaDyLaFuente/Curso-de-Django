from django.contrib import admin

# precisa importar as models primeiro
from .models import Curso, Avaliacao

@admin.register(Curso)
class CursoAdmin(admin.ModelsAdmin):
    list_display = {"titulo", "url", "criacao", "atualizacao", "ativo"}

admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = {"curso", "nome", "email", "avalizao", "criacao", "atualizacao", "ativo"}
