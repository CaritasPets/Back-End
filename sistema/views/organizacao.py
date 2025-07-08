from rest_framework.viewsets import ModelViewSet
from ..models import Organizacao
from ..serializers import OrganizacaoSerializer


class OrganizacaoViewSet(ModelViewSet):
   queryset = Organizacao.objects.all()
   serializer_class = OrganizacaoSerializer