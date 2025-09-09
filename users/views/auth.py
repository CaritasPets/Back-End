from rest_framework import status 
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..serializers import LoginSerializer
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from ..models import User

class LoginView(APIView):
    """
    View para login de usuários
    """
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(
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


class LogoutView(APIView):
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