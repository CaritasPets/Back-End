from django.db import models 

from .organizacao import Organizacao
from .raca import Raca
from .usuario import Usuario
from .porte import Porte

class Pet(models.Model):
    tipo = models.CharField(max_length=25, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False, default='2000-01-01')
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