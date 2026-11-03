from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'refeitorio'

urlpatterns = [
    path('', TemplateView.as_view(template_name='refeitorio/home.html'), name='home'),

    # Turmas
    path('turmas/', views.TurmaListView.as_view(), name='turma_list'),
    path('turmas/nova/', views.TurmaCreateView.as_view(), name='turma_create'),
    path('turmas/<int:pk>/', views.TurmaDetailView.as_view(), name='turma_detail'),
    path('turmas/<int:pk>/editar/', views.TurmaUpdateView.as_view(), name='turma_update'),
    path('turmas/<int:pk>/excluir/', views.TurmaDeleteView.as_view(), name='turma_delete'),

    # Alunos
    path('alunos/', views.AlunoListView.as_view(), name='aluno_list'),
    path('alunos/novo/', views.AlunoCreateView.as_view(), name='aluno_create'),
    path('alunos/<int:pk>/', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('alunos/<int:pk>/editar/', views.AlunoUpdateView.as_view(), name='aluno_update'),
    path('alunos/<int:pk>/excluir/', views.AlunoDeleteView.as_view(), name='aluno_delete'),

    # Refeições
    path('refeicoes/', views.RefeicaoListView.as_view(), name='refeicao_list'),
    path('refeicoes/nova/', views.RefeicaoCreateView.as_view(), name='refeicao_create'),
    path('refeicoes/<int:pk>/excluir/', views.RefeicaoDeleteView.as_view(), name='refeicao_delete'),

    # Relatório
    path('relatorio/', views.RelatorioView.as_view(), name='relatorio'),
]