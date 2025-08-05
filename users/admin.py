from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User, PerfilVoluntario, PerfilOrganizacao


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Admin customizado para o modelo User
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'is_active', 'date_joined')
    list_filter = ('tipo_usuario', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'cpf')
    ordering = ('-date_joined',)
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'cpf', 'telefone', 'endereco', 'data_nascimento')
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'fields': ('tipo_usuario', 'cpf', 'telefone', 'endereco', 'data_nascimento')
        }),
    )


@admin.register(PerfilVoluntario)
class PerfilVoluntarioAdmin(admin.ModelAdmin):
    """
    Admin para o modelo PerfilVoluntario
    """
    list_display = ('user', 'get_user_name', 'ativo', 'data_cadastro')
    list_filter = ('ativo', 'data_cadastro', 'organizacoes')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'especialidades')
    filter_horizontal = ('organizacoes',)
    readonly_fields = ('data_cadastro',)
    
    def get_user_name(self, obj):
        return obj.user.get_full_name() or obj.user.username
    get_user_name.short_description = 'Nome'
    
    fieldsets = (
        ('Usuário', {
            'fields': ('user',)
        }),
        ('Informações do Voluntário', {
            'fields': ('especialidades', 'disponibilidade', 'ativo')
        }),
        ('Organizações', {
            'fields': ('organizacoes',)
        }),
        ('Datas', {
            'fields': ('data_cadastro',),
            'classes': ('collapse',)
        }),
    )


@admin.register(PerfilOrganizacao)
class PerfilOrganizacaoAdmin(admin.ModelAdmin):
    """
    Admin para o modelo PerfilOrganizacao
    """
    list_display = ('user', 'get_organizacao_name', 'responsavel', 'cargo', 'data_cadastro')
    list_filter = ('data_cadastro',)
    search_fields = ('user__username', 'organizacao__nome', 'responsavel', 'cargo')
    readonly_fields = ('data_cadastro',)
    
    def get_organizacao_name(self, obj):
        return obj.organizacao.nome
    get_organizacao_name.short_description = 'Organização'
    
    fieldsets = (
        ('Usuário', {
            'fields': ('user',)
        }),
        ('Organização', {
            'fields': ('organizacao',)
        }),
        ('Responsável', {
            'fields': ('responsavel', 'cargo')
        }),
        ('Datas', {
            'fields': ('data_cadastro',),
            'classes': ('collapse',)
        }),
    )
