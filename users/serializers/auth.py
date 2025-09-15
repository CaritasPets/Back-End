from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from users.models import User
from uploader.serializers.image import ImageSerializer


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
    )
    foto_perfil = serializers.UUIDField(required=False, write_only=True)
    
    class Meta:
        model = User
        fields = (
            'username', 'password', 'email', 'nome', 'cpf', 'telefone', 'data_nascimento', 'foto_perfil'
        )
    
    def create(self, validated_data):
        foto_perfil_id = validated_data.pop('foto_perfil', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            nome=validated_data.get('nome'),
            cpf=validated_data.get('cpf'),
            telefone=validated_data.get('telefone'),
            data_nascimento=validated_data.get('data_nascimento'),
        )

        # Set profile picture if provided
        if foto_perfil_id:
            try:
                from uploader.models import Image
                image = Image.objects.get(attachment_key=foto_perfil_id)
                user.foto_perfil = image
                user.save()
            except Image.DoesNotExist:
                pass  # Ignore if image doesn't exist

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
    foto_perfil = ImageSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'nome',
            'cpf', 'telefone', 'data_nascimento', 'date_joined', 'foto_perfil'
        )
        read_only_fields = ('id', 'username', 'date_joined')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('request') and self.context['request'].method in ['PUT', 'PATCH']:
            self.fields['foto_perfil'] = serializers.UUIDField(required=False, write_only=True)

    def update(self, instance, validated_data):
        foto_perfil_id = validated_data.pop('foto_perfil', None)
        user = super().update(instance, validated_data)

        # Set profile picture if provided
        if foto_perfil_id:
            try:
                from uploader.models import Image
                image = Image.objects.get(attachment_key=foto_perfil_id)
                user.foto_perfil = image
                user.save()
            except Image.DoesNotExist:
                pass  # Ignore if image doesn't exist

        return user