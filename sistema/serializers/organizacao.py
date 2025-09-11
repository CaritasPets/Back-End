from rest_framework.serializers import ModelSerializer
from ..models import Organizacao


class OrganizacaoSerializer(ModelSerializer):
    class Meta:
       model = Organizacao
       fields = "__all__"
       depth = 1
    def create(self, validated_data):
        user = self.context["request"].user
        return Organizacao.objects.create(admin=user, **validated_data)

