from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from uploader.models import Image

class Organization(AbstractUser):
    telefone = models.CharField(max_length=11, blank=False, null=False, default='')
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)

    foto_perfil = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Foto de Perfil",
        related_name="oraganizações"
    )
    groups = models.ManyToManyField(
        Group,
        related_name="organization_group",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="organization_permissions",
        blank=True
    )

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        verbose_name='Organização'
        verbose_name_plural='Organizações'