from rest_framework.viewsets import ModelViewSet
from rest_framework import parsers
from ..models import Pet
from ..models import Perdidos
from ..serializers import PetSerializer
from ..serializers import PerdidosSerializer
from sistema.permissions import CanCreatePet


class PetViewSet(ModelViewSet):
   queryset = Pet.objects.all()
   serializer_class = PetSerializer
   permission_classes = [CanCreatePet]

   def perform_create(self, serializer):
      org = self.request.user.organization_admin.first()
      serializer.save(org=org)

class PerdidosViewSet(ModelViewSet):
   queryset = Perdidos.objects.all()
   serializer_class = PerdidosSerializer
   permission_classes = [CanCreatePet]

   def perform_create(self, serializer):
      serializer.save(dono = self.request.user)