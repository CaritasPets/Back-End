from rest_framework_simplejwt.views import TokenObtainPairView
from ..models import User

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