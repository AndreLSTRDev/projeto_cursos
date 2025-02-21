from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    formacao = models.TextField()
    experiencia = models.TextField()
    minicurriculo = models.TextField()
    foto = models.ImageField(upload_to='professores')
    bio = models.TextField(blank=True, null=True)
    areas_interesse = models.CharField(max_length=200, blank=True, null=True)
    contato = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    descricao_detalhada = models.TextField()
    carga_horaria = models.IntegerField()
    categoria = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50, choices=(
        ('basico', 'Básico'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    ))
    requisitos = models.TextField()
    data_inicio = models.DateField()
    instrutores = models.ManyToManyField(Professor)
    alunos = models.ManyToManyField(User, related_name='cursos_matriculados')
    materiais = models.FileField(upload_to='cursos')
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    duracao = models.IntegerField()
    video = models.FileField(upload_to='aulas')
    materiais = models.FileField(upload_to='aulas')
    ordem = models.IntegerField()
    tipo = models.CharField(max_length=50, choices=(
        ('video', 'Vídeo'),
        ('texto', 'Texto'),
        ('exercicio', 'Exercício'),
        ('link_externo', 'Link Externo'),
    ))
    link_externo = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo