from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    UserRegistrationView,
    LoginView,
    UserProfileView,
    LogoutView,
    CustomTokenObtainPairView,
)
from users.views.user import user_info, change_password

app_name = 'users'

urlpatterns = [
    # Registro
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    
    # Autenticação
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # JWT Tokens
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    
    # Perfil do usuário
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('info/', user_info, name='user-info'),
    path('change-password/', change_password, name='change-password'),
]