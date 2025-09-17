from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from ..models import Pet
from ..models import Perdidos
from uploader.models import Image
from uploader.serializers import ImageSerializer

class PetSerializer(ModelSerializer):
    foto = ImageSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = ['nome', 'especie', 'castrado', 'genero', 'vacinado', 'peso', 'porte', 'raca', 'foto']
        read_only_fields = ['org']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('request') and self.context['request'].method in ['POST', 'PUT', 'PATCH']:
            self.fields['foto'] = serializers.UUIDField(required=False, write_only=True)

    def create(self, validated_data):
        foto_id = validated_data.pop('foto', None)
        instance = super().create(validated_data)
        if foto_id:
            try:
                image = Image.objects.get(attachment_key=foto_id)
                instance.foto = image
                instance.save()
            except Image.DoesNotExist:
                pass
        return instance

    def update(self, instance, validated_data):
        foto_id = validated_data.pop('foto', None)
        instance = super().update(instance, validated_data)
        if foto_id:
            try:
                image = Image.objects.get(attachment_key=foto_id)
                instance.foto = image
                instance.save()
            except Image.DoesNotExist:
                pass
        return instance

class PerdidosSerializer(ModelSerializer):
    foto = ImageSerializer(read_only=True)

    class Meta:
        model = Perdidos
        fields = ['nome', 'especie', 'local', 'caracteristicas', 'genero', 'foto']
        read_only_fields = ['dono']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('request') and self.context['request'].method in ['POST', 'PUT', 'PATCH']:
            self.fields['foto'] = serializers.UUIDField(required=False, write_only=True)

    def create(self, validated_data):
        foto_id = validated_data.pop('foto', None)
        instance = super().create(validated_data)
        if foto_id:
            try:
                image = Image.objects.get(attachment_key=foto_id)
                instance.foto = image
                instance.save()
            except Image.DoesNotExist:
                pass
        return instance

    def update(self, instance, validated_data):
        foto_id = validated_data.pop('foto', None)
        instance = super().update(instance, validated_data)
        if foto_id:
            try:
                image = Image.objects.get(attachment_key=foto_id)
                instance.foto = image
                instance.save()
            except Image.DoesNotExist:
                pass
        return instance