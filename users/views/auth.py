from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.contrib.auth import login
from users.models import User
from users.serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
)


class UserRegistrationView(generics.CreateAPIView):
    """
    View para registro de usuários comuns
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
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


class UserLoginView(APIView):
    """
    View para login de usuários
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        # Fazer login
        login(request, user)
        
        # Gerar tokens JWT
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'Login realizado com sucesso!',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    """
    View para logout de usuários
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response({
                'message': 'Logout realizado com sucesso!'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': 'Token inválido'
            }, status=status.HTTP_400_BAD_REQUEST)


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


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View customizada para obter tokens JWT
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            # Adicionar informações do usuário na resposta
            username = request.data.get('username')
            try:
                user = User.objects.get(username=username)
                response.data['user'] = {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'nome': user.nome,
                }
            except User.DoesNotExist:
                pass
        
        return response