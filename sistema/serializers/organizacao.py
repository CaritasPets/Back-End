from rest_framework.serializers import ModelSerializer
from ..models import Organizacao


class OrganizacaoSerializer(ModelSerializer):
    class Meta:
       model = Organizacao
       fields = "__all__"
       read_only_fields = ['admin']
       depth = 2

    def create(self, validated_data):
       user = self.context["request"].user
       organizacao = Organizacao.objects.create(admin=user, **validated_data)
       return organizacao

