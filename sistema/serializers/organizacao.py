from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Organizacao
from uploader.serializers.image import ImageSerializer
from uploader.models import Image


class OrganizacaoSerializer(ModelSerializer):
    foto_perfil = ImageSerializer(read_only=True)

    class Meta:
       model = Organizacao
       fields = "__all__"
       depth = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('request') and self.context['request'].method in ['POST', 'PUT', 'PATCH']:
            self.fields['foto_perfil'] = serializers.UUIDField(required=False, write_only=True)

    def create(self, validated_data):
        foto_perfil_id = validated_data.pop('foto_perfil', None)
        user = self.context["request"].user
        organizacao = Organizacao.objects.create(admin=user, **validated_data)

        # Set profile picture if provided
        if foto_perfil_id:
            try:
                from uploader.models import Image
                image = Image.objects.get(attachment_key=foto_perfil_id)
                organizacao.foto_perfil = image
                organizacao.save()
            except Image.DoesNotExist:
                pass  # Ignore if image doesn't exist

        return organizacao

    def update(self, instance, validated_data):
        foto_perfil_id = validated_data.pop('foto_perfil', None)
        organizacao = super().update(instance, validated_data)

        # Set profile picture if provided
        if foto_perfil_id:
            try:
                from uploader.models import Image
                image = Image.objects.get(attachment_key=foto_perfil_id)
                organizacao.foto_perfil = image
                organizacao.save()
            except Image.DoesNotExist:
                pass  # Ignore if image doesn't exist

        return organizacao

