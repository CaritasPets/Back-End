from rest_framework.serializers import ModelSerializer
from ..models import Membro

class MembroSerializer(ModelSerializer):
    class Meta:
        model = Membro
        fields = "__all__"