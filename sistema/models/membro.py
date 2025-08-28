from django.db import models
from .organizacao import Organizacao
from users.models import User

class Membro(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    organization = models.ForeignKey(Organizacao, on_delete=models.PROTECT, null=False)
    permission = models.CharField(max_length=5, choices=[
        ('admin', 'Administrador'),
        ('colab', 'Colaborador')
    ])
    