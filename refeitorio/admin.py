from django.contrib import admin
from .models import Aluno, Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'dia_semana', 'turno')
    list_filter = ('dia_semana', 'turno')
    search_fields = ('turma',)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_aluno', 'matricula', 'turma', 'situacao')
    list_filter = ('turma', 'situacao')
    search_fields = ('nome_aluno', 'matricula')

from .models import Aluno, Turma, Refeicao


@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'data')
    list_filter = ('data',)