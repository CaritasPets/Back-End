from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from ..models import Organization
from ..serializers import (
    OrganizationRegistrationSerializer,
    OrganizationProfileSerializer
)

class OrganizationRegistrationView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        organization=serializer.save()

        refresh = RefreshToken.for_user(organization)
        
        return Response({
            'message': 'ONG criada com sucesso!',
            'organization': {
                'id': organization.id,
                'username': organization.username,
                'email': organization.email,
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        })

#class OrganizationProfileView():
