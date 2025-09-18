from django.db import models 

from .organizacao import Organizacao
from users.models import User
from uploader.models import Image

class Pet(models.Model):
    PORTE_CHOICES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande')
    ]
    VACINADO_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Nao'),
        ('parcialmente', 'Parcialmente'),
        ('nao-sei', 'Não sei')
    ]
    CASTRADO_CHOICES = [
        ('sim', 'sim'),
        ('nao', 'nao')
    ]
    GENERO_CHOICES = [
        ('macho', 'macho'),
        ('femea', 'femea')
    ]      
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('passaro', 'Pássaro'),
        ('outro', 'Outro')
    ]

    nome = models.CharField(max_length=50, null=False, blank=False, default='')
    especie = models.CharField(max_length=25, choices=ESPECIE_CHOICES, null=False, blank=False)
    castrado = models.CharField(max_length=3, choices=CASTRADO_CHOICES, default='nao')
    genero = models.CharField(max_length=5, choices=GENERO_CHOICES, default='macho')
    vacinado = models.CharField(max_length=12, choices=VACINADO_CHOICES, default='nao')
    peso = models.DecimalField(max_digits=5, decimal_places=3 ,null=True, blank=True)
    porte = models.CharField(max_length=7, choices=PORTE_CHOICES, default='pequeno')
    raca = models.CharField(max_length=100, blank=True, null=True)
    org = models.ForeignKey(
        Organizacao, on_delete=models.PROTECT, related_name="pets_organizacao"
    )
    foto = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return f"{self.especie} ({self.org})"

class Perdidos(models.Model):
    GENERO_CHOICES = [
        ('macho', 'macho'),
        ('femea', 'femea')
    ]      
    ESPECIE_CHOICES = [
        ('cachorro', 'Cachorro'),
        ('gato', 'Gato'),
        ('passaro', 'Pássaro'),
        ('outro', 'Outro')
    ]

    nome = models.CharField(max_length=50, null=False, blank=False, default='')
    especie = models.CharField(max_length=25, choices=ESPECIE_CHOICES, null=False, blank=False)
    local = models.CharField(max_length=100, null=False, blank=False, default='')
    caracteristicas = models.CharField(max_length=300, null=True, blank=True)
    genero = models.CharField(max_length=5, choices=GENERO_CHOICES, default='macho')
    dono = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='perdidos_user',
        default=None
    )
    foto = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return f"{self.especie} ({self.dono})"


