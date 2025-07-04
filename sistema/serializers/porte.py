from rest_framework.serializers import ModelSerializer
from models import Porte


class PorteSerializer(ModelSerializer):
   class Meta:
       model = Porte
       fields = "__all__"
