from django.db import models

class Aluno(models.Model):

    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50, primary_key=True)

class Form(models.Model):
    
    TIPO = (
        (0, 'Jantar'),
        (1, 'Almoço'),
    )
    professor = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    turma = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    tipo_de_refeicao = models.IntegerField(choices=TIPO)
    status = models.BooleanField()
    alunos = models.ManyToManyField(Aluno, related_name='forms')
