from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Organizacao
from ..serializers import OrganizacaoSerializer



class OrganizacaoViewSet(ModelViewSet):
   queryset = Organizacao.objects.all()
   serializer_class = OrganizacaoSerializer
   permission_classes = [IsAuthenticated]

   def get_serializer_context(self):
      context = super().get_serializer_context()
      context["request"] = self.request
      return context

