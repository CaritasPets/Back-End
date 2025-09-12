from django.db import models 

from .organizacao import Organizacao
from .raca import Raca
from users.models import User
from uploader.models import Image

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
    TIPO_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('outro', 'Outro')
    ]

    nome = models.CharField(max_length=50, null=False, blank=False, default='')
    tipo = models.CharField(max_length=25, choices=TIPO_CHOICES, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default='2000-01-01')
    castrado = models.CharField(max_length=1, choices=CASTRADO_CHOICES, default='n')
    genero = models.CharField(max_length=1, choices=SEXO_CHOICES, default='m')
    vacinado = models.CharField(max_length=1, choices=VACINADO_CHOICES, default='n')
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, related_name="pets"
    )
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES, default='p')
    org = models.ForeignKey(
        Organizacao, on_delete=models.PROTECT, related_name="pets_organizacao"
    )
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
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
    TIPO_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('outro', 'Outro')
    ]

    nome = models.CharField(max_length=50, null=False, blank=False, default='')
    tipo = models.CharField(max_length=25, choices=TIPO_CHOICES, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default='2000-01-01')
    castrado = models.CharField(max_length=1, choices=CASTRADO_CHOICES, default='n')
    genero = models.CharField(max_length=1, choices=SEXO_CHOICES, default='m')
    vacinado = models.CharField(max_length=1, choices=VACINADO_CHOICES, default='n')
    raca = models.ForeignKey(
        Raca, on_delete=models.PROTECT, related_name="pets_perdidos"
    )
    porte = models.CharField(max_length=1, choices=PORTE_CHOICES, default='p')
    dono = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='perdidos_user',
        default=None
    )
    local = models.CharField(max_length=100, null=False, blank=False, default='')
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None,
    )

    def __str__(self):
        return f"{self.tipo} ({self.org})"

