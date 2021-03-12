from django.db import models

class Aniversario(models.Model):
    nome = models.CharField(max_length=30)
    data_aniversario = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
