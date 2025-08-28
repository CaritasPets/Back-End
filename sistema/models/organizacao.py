from django.db import models
from users.models import User

class Organizacao(models.Model):
    nome = models.CharField(max_length=45, unique=True, null=False, default='Nome da Organização')
    cnpj = models.CharField(max_length=14, unique=True, null=False,)
    email = models.CharField(max_length=320, unique=True, null=False)
    senha = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    users = models.ManyToManyField(User)
    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = 'Organização'
        verbose_name_plural = 'Organizações'
