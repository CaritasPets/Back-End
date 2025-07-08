from rest_framework.viewsets import ModelViewSet
from ..models import Porte
from ..serializers import PorteSerializer


class PorteViewSet(ModelViewSet):
   queryset = Porte.objects.all()
   serializer_class = PorteSerializer