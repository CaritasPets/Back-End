from django.db import models 

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    username = models.CharField(max_length=45, unique=True, null=False, blank=False)
    senha = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    email = models.CharField(max_length=320, unique=True, null=False, blank=False)
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=100, null=True, blank=True)

    data_nascimento = models.DateField(null=False, blank=False, default='2000-01-01')

    def __str__(self):
        return f'{self.username} ({self.cpf})'


