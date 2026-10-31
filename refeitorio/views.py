from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)
from .models import Aluno, Turma


# ---------- TURMAS ----------

class TurmaListView(ListView):
    model = Turma
    template_name = 'refeitorio/turma_lista.html'

class TurmaDetailView(DetailView):
    model = Turma


class TurmaCreateView(CreateView):
    model = Turma
    fields = ['turma', 'dia_semana', 'turno']
    template_name = 'refeitorio/form.html'
    success_url = reverse_lazy('refeitorio:turma_list')
    titulo = 'Nova turma'


class TurmaUpdateView(UpdateView):
    model = Turma
    fields = ['turma', 'dia_semana', 'turno']
    template_name = 'refeitorio/form.html'
    success_url = reverse_lazy('refeitorio:turma_list')
    titulo = 'Editar turma'


class TurmaDeleteView(DeleteView):
    model = Turma
    template_name = 'refeitorio/delete.html'
    success_url = reverse_lazy('refeitorio:turma_list')


# ---------- ALUNOS ----------
class AlunoListView(ListView):
    model = Aluno
    template_name = 'refeitorio/aluno_lista.html'


class AlunoDetailView(DetailView):
    model = Aluno


class AlunoCreateView(CreateView):
    model = Aluno
    fields = ['nome_aluno', 'matricula', 'turma', 'situacao']
    template_name = 'refeitorio/form.html'
    success_url = reverse_lazy('refeitorio:aluno_list')
    titulo = 'Novo aluno'


class AlunoUpdateView(UpdateView):
    model = Aluno
    fields = ['nome_aluno', 'matricula', 'turma', 'situacao']
    template_name = 'refeitorio/form.html'
    success_url = reverse_lazy('refeitorio:aluno_list')
    titulo = 'Editar aluno'


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'refeitorio/delete.html'
    success_url = reverse_lazy('refeitorio:aluno_list')