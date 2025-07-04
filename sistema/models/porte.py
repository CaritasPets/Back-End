from django.db import models

class Porte(models.Model):
    tipo = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.tipo}'