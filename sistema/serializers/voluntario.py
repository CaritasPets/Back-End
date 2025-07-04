from rest_framework.serializers import ModelSerializer
from models import Voluntario


class VoluntarioSerializer(ModelSerializer):
   class Meta:
       model = Voluntario
       fields = "__all__"
