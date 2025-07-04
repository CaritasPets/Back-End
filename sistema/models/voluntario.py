from django.db import models

class Voluntario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False)
    username = models.CharField(max_length=45, null=False, blank=False, unique=True)
    senha = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f'{self.username}'