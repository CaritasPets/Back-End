from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from ..models import Pet
from ..models import Perdidos
from uploader.models import Image
from uploader.serializers import ImageSerializer

class PetSerializer(ModelSerializer):
   class Meta:
       model = Pet
       fields = "__all__"
   foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
   foto = ImageSerializer(required=False, read_only=True)

class PerdidosSerializer(ModelSerializer):
   class Meta:
       model = Perdidos
       fields = "__all__"
   foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
   foto = ImageSerializer(required=False, read_only=True)