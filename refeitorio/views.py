from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView,
)
from django.db.models import Count, Q
from django.utils.dateparse import parse_date
from django.views.generic import TemplateView
from .models import Aluno, Turma, Refeicao


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

# ---------- REGISTRO ----------
class RefeicaoListView(ListView):
    model = Refeicao
    template_name = 'refeitorio/refeicao_lista.html'


class RefeicaoCreateView(CreateView):
    model = Refeicao
    fields = ['aluno', 'data']
    template_name = 'refeitorio/form.html'
    success_url = reverse_lazy('refeitorio:refeicao_list')
    titulo = 'Registrar refeição'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['data'].widget.input_type = 'date'
        return form


class RefeicaoDeleteView(DeleteView):
    model = Refeicao
    template_name = 'refeitorio/delete.html'
    success_url = reverse_lazy('refeitorio:refeicao_list')


# ---------- RELATÓRIO ----------
class RelatorioView(TemplateView):
    template_name = 'refeitorio/relatorio.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        dias = [d[0] for d in Turma.DIAS_SEMANA]
        dia = self.request.GET.get('dia')
        data = parse_date(self.request.GET.get('data', ''))

        ctx['dias'] = dias
        ctx['dia'] = dia
        ctx['data'] = data

        if dia in dias:
            filtro_ref = Q(alunos__refeicoes__data=data) if data else Q()
            turmas = Turma.objects.filter(dia_semana=dia).annotate(
                esperados=Count('alunos', filter=Q(alunos__situacao=True), distinct=True),
                realizadas=Count('alunos__refeicoes', filter=filtro_ref, distinct=True),
            )
            ctx['turmas'] = turmas
            ctx['total_esperados'] = sum(t.esperados for t in turmas)
            ctx['total_realizadas'] = sum(t.realizadas for t in turmas)
        return ctx