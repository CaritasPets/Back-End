from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from users.serializers import (
    UserRegistrationSerializer,
    UserProfileSerializer,
)

class UserRegistrationView(generics.CreateAPIView):
    """
    View para registro de usuários comuns
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Gerar tokens JWT
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'Usuário criado com sucesso!',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)



class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    View para visualizar e atualizar perfil do usuário
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'user': serializer.data
        })
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response({
            'message': 'Perfil atualizado com sucesso!',
            'user': serializer.data
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    """
    View simples para obter informações do usuário autenticado
    """
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'is_authenticated': True,
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    """
    View para alterar senha do usuário
    """
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    
    if not old_password or not new_password:
        return Response({
            'error': 'Senha atual e nova senha são obrigatórias'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not user.check_password(old_password):
        return Response({
            'error': 'Senha atual incorreta'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user.set_password(new_password)
    user.save()
    
    return Response({
        'message': 'Senha alterada com sucesso!'
    }, status=status.HTTP_200_OK)