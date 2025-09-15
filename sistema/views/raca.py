from rest_framework.viewsets import ModelViewSet
from ..models import Raca
from ..serializers import RacaSerializer
from rest_framework.permissions import AllowAny

class RacaViewSet(ModelViewSet):
   queryset = Raca.objects.all()
   serializer_class = RacaSerializer
   permission_classes = [AllowAny]