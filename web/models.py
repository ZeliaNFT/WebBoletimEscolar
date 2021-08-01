from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField('Nome Aluno', max_length=100)
    nota = models.DecimalField('Nota', decimal_places=2, max_digits=8)
    situacao = models.CharField('Situação', max_length=100)

    def __str__(self):
        return self.nome

