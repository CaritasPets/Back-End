from rest_framework.serializers import ModelSerializer
from models import Pet
from models import Perdidos


class PetSerializer(ModelSerializer):
   class Meta:
       model = Pet
       fields = "__all__"
    
class PerdidosSerializer(ModelSerializer):
   class Meta:
       model = Perdidos
       fields = "__all__"
