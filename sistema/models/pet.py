from django.db import models 

from .organizacao import Organizacao
from .raca import Raca
from .usuario import Usuario
from .porte import Porte
from .voluntario import Voluntario

class Pet(models.Model):
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
    porte = models.ForeignKey(
        Porte, on_delete=models.PROTECT, related_name="pets"
    )
    org = models.ForeignKey(
        Organizacao, on_delete=models.PROTECT, related_name="pets"
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name="pets"
    )

class Perdidos(models.Model):
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
    porte = models.ForeignKey(
        Porte, on_delete=models.PROTECT, related_name="pets_perdidos"
    )
    org = models.ForeignKey(
        Organizacao, on_delete=models.PROTECT, related_name="pets_perdidos"
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.PROTECT, related_name="pets_perdidos"
    )
    voluntario = models.ForeignKey(
        Voluntario, on_delete=models.PROTECT, related_name="pets_perdidos"
    )