from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from users.models import User, PerfilVoluntario, PerfilOrganizacao
from sistema.models import Organizacao


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer para registro de usuários comuns
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = (
            'username', 'password', 'password2', 'email', 'first_name',
            'last_name', 'cpf', 'telefone', 'endereco', 'data_nascimento'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Os campos de senha não coincidem."}
            )
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            cpf=validated_data.get('cpf'),
            telefone=validated_data.get('telefone'),
            endereco=validated_data.get('endereco'),
            data_nascimento=validated_data.get('data_nascimento'),
            tipo_usuario='comum'
        )
        return user


class VoluntarioRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer para registro de voluntários
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    especialidades = serializers.CharField(required=False, allow_blank=True)
    disponibilidade = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = User
        fields = (
            'username', 'password', 'password2', 'email', 'first_name',
            'last_name', 'cpf', 'telefone', 'endereco', 'data_nascimento',
            'especialidades', 'disponibilidade'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Os campos de senha não coincidem."}
            )
        return attrs
    
    def create(self, validated_data):
        especialidades = validated_data.pop('especialidades', '')
        disponibilidade = validated_data.pop('disponibilidade', '')
        validated_data.pop('password2', None)
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            cpf=validated_data.get('cpf'),
            telefone=validated_data.get('telefone'),
            endereco=validated_data.get('endereco'),
            data_nascimento=validated_data.get('data_nascimento'),
            tipo_usuario='voluntario'
        )
        
        # Criar perfil de voluntário
        PerfilVoluntario.objects.create(
            user=user,
            especialidades=especialidades,
            disponibilidade=disponibilidade
        )
        
        return user


class OrganizacaoRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer para registro de organizações
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    # Campos da organização
    nome_organizacao = serializers.CharField(required=True)
    cnpj = serializers.CharField(required=True)
    email_organizacao = serializers.EmailField(required=True)
    telefone_organizacao = serializers.CharField(required=False, allow_blank=True)
    endereco_organizacao = serializers.CharField(required=True)
    descricao_organizacao = serializers.CharField(required=False, allow_blank=True)
    
    # Campos do responsável
    responsavel = serializers.CharField(required=True)
    cargo = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = User
        fields = (
            'username', 'password', 'password2', 'email', 'first_name',
            'last_name', 'cpf', 'telefone', 'endereco',
            'nome_organizacao', 'cnpj', 'email_organizacao',
            'telefone_organizacao', 'endereco_organizacao', 'descricao_organizacao',
            'responsavel', 'cargo'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Os campos de senha não coincidem."}
            )
        
        # Verificar se CNPJ já existe
        if Organizacao.objects.filter(cnpj=attrs['cnpj']).exists():
            raise serializers.ValidationError(
                {"cnpj": "Uma organização com este CNPJ já está cadastrada."}
            )
        
        return attrs
    
    def create(self, validated_data):
        # Extrair dados da organização
        org_data = {
            'nome': validated_data.pop('nome_organizacao'),
            'cnpj': validated_data.pop('cnpj'),
            'email': validated_data.pop('email_organizacao'),
            'telefone': validated_data.pop('telefone_organizacao', ''),
            'endereco': validated_data.pop('endereco_organizacao'),
            'descricao': validated_data.pop('descricao_organizacao', ''),
            'senha': validated_data['password']  # Manter compatibilidade com modelo existente
        }
        
        # Extrair dados do perfil
        responsavel = validated_data.pop('responsavel')
        cargo = validated_data.pop('cargo', '')
        validated_data.pop('password2', None)
        
        # Criar usuário
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            cpf=validated_data.get('cpf'),
            telefone=validated_data.get('telefone'),
            endereco=validated_data.get('endereco'),
            tipo_usuario='organizacao'
        )
        
        # Criar organização
        organizacao = Organizacao.objects.create(**org_data)
        
        # Criar perfil de organização
        PerfilOrganizacao.objects.create(
            user=user,
            organizacao=organizacao,
            responsavel=responsavel,
            cargo=cargo
        )
        
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer para login de usuários
    """
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )
            
            if not user:
                msg = 'Não foi possível fazer login com as credenciais fornecidas.'
                raise serializers.ValidationError(msg, code='authorization')
            
            if not user.is_active:
                msg = 'Conta de usuário desativada.'
                raise serializers.ValidationError(msg, code='authorization')
            
            attrs['user'] = user
            return attrs
        else:
            msg = 'Deve incluir "username" e "password".'
            raise serializers.ValidationError(msg, code='authorization')


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer para perfil do usuário
    """
    perfil_voluntario = serializers.SerializerMethodField()
    perfil_organizacao = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'cpf', 'telefone', 'endereco', 'data_nascimento',
            'tipo_usuario', 'date_joined', 'perfil_voluntario',
            'perfil_organizacao'
        )
        read_only_fields = ('id', 'username', 'date_joined', 'tipo_usuario')
    
    def get_perfil_voluntario(self, obj):
        if hasattr(obj, 'perfil_voluntario'):
            perfil = obj.perfil_voluntario
            return {
                'especialidades': perfil.especialidades,
                'disponibilidade': perfil.disponibilidade,
                'ativo': perfil.ativo,
                'organizacoes': [org.nome for org in perfil.organizacoes.all()]
            }
        return None
    
    def get_perfil_organizacao(self, obj):
        if hasattr(obj, 'perfil_organizacao'):
            perfil = obj.perfil_organizacao
            return {
                'organizacao': {
                    'nome': perfil.organizacao.nome,
                    'cnpj': perfil.organizacao.cnpj,
                    'email': perfil.organizacao.email,
                    'telefone': perfil.organizacao.telefone,
                    'endereco': perfil.organizacao.endereco,
                    'descricao': perfil.organizacao.descricao,
                },
                'responsavel': perfil.responsavel,
                'cargo': perfil.cargo,
            }
        return None