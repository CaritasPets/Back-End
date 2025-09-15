from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import parsers
from sistema.permissions import IsOrganizationAdminOrReadOnly
from ..models import Organizacao
from ..serializers import OrganizacaoSerializer



class OrganizacaoViewSet(ModelViewSet):
   queryset = Organizacao.objects.all()
   serializer_class = OrganizacaoSerializer

   def get_serializer_context(self):
      context = super().get_serializer_context()
      context["request"] = self.request
      return context
   
   def get_permissions(self):
      if self.action == "list":
         return [AllowAny()]
      elif self.action == "create":
         return [IsAuthenticated()]
      else:
         return [IsAuthenticated(), IsOrganizationAdminOrReadOnly()]

         