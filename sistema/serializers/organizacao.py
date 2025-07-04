from rest_framework.serializers import ModelSerializer
from models import Organizacao


class OrganizacaoSerializer(ModelSerializer):
   class Meta:
       model = Organizacao
       fields = "__all__"
