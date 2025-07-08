from rest_framework.viewsets import ModelViewSet
from ..models import Raca
from ..serializers import RacaSerializer


class RacaViewSet(ModelViewSet):
   queryset = Raca.objects.all()
   serializer_class = RacaSerializer