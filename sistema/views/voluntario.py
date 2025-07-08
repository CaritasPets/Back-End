from rest_framework.viewsets import ModelViewSet
from ..models import Voluntario
from ..serializers import VoluntarioSerializer


class VoluntarioViewSet(ModelViewSet):
   queryset = Voluntario.objects.all()
   serializer_class = VoluntarioSerializer