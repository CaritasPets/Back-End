from django.db import models 

from .organizacao import Organizacao
from .raca import Raca
from uploader.models import Image
from users.models import User

class Pet(models.Model):
    PORTE_CHOICES = [
        ('p', 'Pequeno'),
        ('m', 'Médio'),
        ('g', 'Grande')
    ]
    VACINADO_CHOICES = [
        ('s', 'sim'),
        ('n', 'nao')
    ]
    CASTRADO_CHOICES = [
        ('s', 'sim'),
        ('n', 'nao')
    ]
    SEXO_CHOICES = [
        ('m', 'macho'),
        ('f', 'femea')
    ]
    
    tipo = models.CharField(max_length=25, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default='2000-01-01')
    castrado = models.CharField(max_length=1, choices=CASTRADO_CHOICES, default='n')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='m')
    vacinado = models.CharField(max_length=1, choices=VACINADO_CHOICES, default='n')
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, related_name="pets"
    )
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES, default='p')
    org = models.ForeignKey(
        Organizacao, on_delete=models.PROTECT, related_name="pets"
    )

    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.tipo} ({self.org})"

class Perdidos(models.Model):
    PORTE_CHOICES = [
        ('p', 'Pequeno'),
        ('m', 'Médio'),
        ('g', 'Grande')
    ]
    VACINADO_CHOICES = [
        ('s', 'sim'),
        ('n', 'nao')
    ]
    CASTRADO_CHOICES = [
        ('s', 'sim'),
        ('n', 'nao')
    ]
    SEXO_CHOICES = [
        ('m', 'macho'),
        ('f', 'femea')
    ]      

    tipo = models.CharField(max_length=25, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default='2000-01-01')
    castrado = models.CharField(max_length=1, choices=CASTRADO_CHOICES, default='n')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='m')
    vacinado = models.CharField(max_length=1, choices=VACINADO_CHOICES, default='n')
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, related_name="pets_perdidos"
    )
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES, default='p')
    user = models.ForeignKey(
        User,
        related_name="user",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.tipo} ({self.org})"

