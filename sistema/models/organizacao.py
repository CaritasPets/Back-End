from django.db import models
from users.models import User
from django.conf import settings
from uploader.models import Image

class Organizacao(models.Model):
    admin = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='organization_admin'
    )
    nome = models.CharField(max_length=45, unique=True, null=False, default='Nome da Organização')
    cnpj = models.CharField(max_length=14, unique=True, null=False,)
    email = models.CharField(max_length=320, unique=True, null=False)
    senha = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=False, blank=False)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    faceboook = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    foto_perfil = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Foto de Perfil',
        related_name='organizacoes'
    )

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = 'Organização'
        verbose_name_plural = 'Organizações'
