from rest_framework.viewsets import ModelViewSet
from ..models import Pet
from ..models import Perdidos
from ..serializers import PetSerializer
from ..serializers import PerdidosSerializer


class PetViewSet(ModelViewSet):
   queryset = Pet.objects.all()
   serializer_class = PetSerializer

class PerdidosViewSet(ModelViewSet):
   queryset = Perdidos.objects.all()
   serializer_class = PerdidosSerializer