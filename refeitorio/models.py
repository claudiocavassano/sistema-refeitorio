from django.db import models


class Turma(models.Model):
    DIAS_SEMANA = [
        ('Segunda-feira', 'Segunda-feira'),
        ('Terça-feira', 'Terça-feira'),
        ('Quarta-feira', 'Quarta-feira'),
        ('Quinta-feira', 'Quinta-feira'),
        ('Sexta-feira', 'Sexta-feira'),
    ]
    TURNOS = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
    ]

    turma = models.CharField('Turma', max_length=100, unique=True)
    dia_semana = models.CharField('Dia da semana', max_length=20, choices=DIAS_SEMANA)
    turno = models.CharField('Turno', max_length=10, choices=TURNOS)

    class Meta:
        ordering = ['turma']

    def __str__(self):
        return self.turma


class Aluno(models.Model):
    nome_aluno = models.CharField('Nome', max_length=150)
    matricula = models.CharField('Matrícula', max_length=20, unique=True)
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='alunos',
        verbose_name='Turma',
    )
    situacao = models.BooleanField('Ativo', default=True)

    class Meta:
        ordering = ['nome_aluno']

    def __str__(self):
        return f'{self.nome_aluno} ({self.matricula})'