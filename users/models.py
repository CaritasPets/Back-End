from django.contrib.auth.models import AbstractUser
from django.db import models
from uploader.models import Image


class User(AbstractUser):
    
    ##Modelo de usuário customizado que estende AbstractUser
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='',
        verbose_name='Nome completo'
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        blank=False,
        default='',
        verbose_name='CPF'
    )
    telefone = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        default='',
        verbose_name='Telefone'
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name='Data de Nascimento'
    )
    foto_perfil = models.ImageField(upload_to="images/", blank=True, null=True)
    
    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

