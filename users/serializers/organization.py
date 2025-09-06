from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from ..models import Organization
from uploader.serializers.image import ImageSerializer

class OrganizationRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=Organization.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required=True
    )
    foto_perfil = serializers.UUIDField(required=False, write_only=True)

    class Meta: 
        model=Organization
        fields = (
            'username', 'password', 'email', 'telefone', 'cnpj', 'instagram', 'facebook', 'endereco', 'foto_perfil'
        )
    
    def create(self, validated_data):
        foto_perfil_id = validated_data.pop('foto_perfil', None)
        organization = Organization.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            telefone=validated_data.get('telefone'),
            cnpj=validated_data.get('cnpj'),
            instagram=validated_data.get('instagram'),
            facebook=validated_data.get('facebook'),
            endereco=validated_data.get('endereco')
        )

        if foto_perfil_id:
            try:
                from uploader.models import Image
                image=Image.objects.get(attachment_key=foto_perfil_id)
                organization.foto_perfil = image
                organization.save()
            except Image.DoesNotExist:
                pass
        return organization
    