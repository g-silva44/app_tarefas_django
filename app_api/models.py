from django.db import models


# Create your models here.
class PessoaModel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    class Meta:
        ordering = ['nome']

        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

        db_table = 'pessoa'
