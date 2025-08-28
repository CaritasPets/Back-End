from rest_framework.viewsets import ModelViewSet
from ..serializers import MembroSerializer
from ..models import Membro

class MembroViewSet(ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer
    