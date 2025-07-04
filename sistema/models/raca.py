from django.db import models

class Raca(models.Model):
    tipo = models.CharField(max_length=45)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.tipo}'