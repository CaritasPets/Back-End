from django.contrib.auth.models import AbstractUser
from django.db import models
from sistema.models import Organizacao


class User(AbstractUser):
    """
    Modelo de usuário customizado que estende AbstractUser
    """
    TIPO_USUARIO_CHOICES = [
        ('comum', 'Usuário Comum'),
        ('voluntario', 'Voluntário'),
        ('organizacao', 'Organização'),
    ]
    
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        default='comum',
        verbose_name='Tipo de Usuário'
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        null=True,
        blank=True,
        verbose_name='CPF'
    )
    telefone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name='Telefone'
    )
    endereco = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Endereço'
    )
    data_nascimento = models.DateField(
        null=True,
        blank=True,
        verbose_name='Data de Nascimento'
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_tipo_usuario_display()})"
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class PerfilVoluntario(models.Model):
    """
    Perfil específico para voluntários
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil_voluntario',
        verbose_name='Usuário'
    )
    organizacoes = models.ManyToManyField(
        Organizacao,
        related_name='voluntarios',
        blank=True,
        verbose_name='Organizações'
    )
    especialidades = models.TextField(
        null=True,
        blank=True,
        verbose_name='Especialidades',
        help_text='Descreva suas especialidades e habilidades'
    )
    disponibilidade = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Disponibilidade',
        help_text='Ex: Manhãs, tardes, fins de semana'
    )
    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo'
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )
    
    def __str__(self):
        return f"Voluntário: {self.user.get_full_name() or self.user.username}"
    
    class Meta:
        verbose_name = 'Perfil de Voluntário'
        verbose_name_plural = 'Perfis de Voluntários'


class PerfilOrganizacao(models.Model):
    """
    Perfil específico para organizações
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil_organizacao',
        verbose_name='Usuário'
    )
    organizacao = models.OneToOneField(
        Organizacao,
        on_delete=models.CASCADE,
        related_name='perfil_usuario',
        verbose_name='Organização'
    )
    responsavel = models.CharField(
        max_length=100,
        verbose_name='Responsável',
        help_text='Nome do responsável pela conta'
    )
    cargo = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='Cargo'
    )
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )
    
    def __str__(self):
        return f"Organização: {self.organizacao.nome}"
    
    class Meta:
        verbose_name = 'Perfil de Organização'
        verbose_name_plural = 'Perfis de Organizações'
