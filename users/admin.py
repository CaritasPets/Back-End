from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ##Admin customizado para o modelo User
    list_display = ('username', 'email', 'nome',  'is_active', 'date_joined')
    list_filter = ( 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'nome', 'cpf')
    ordering = ('-date_joined',)
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ( 'cpf', 'telefone', 'data_nascimento')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ( 'cpf', 'telefone', 'data_nascimento')
        }),
    )