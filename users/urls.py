from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from users.views import (
    UserRegistrationView,
    VoluntarioRegistrationView,
    OrganizacaoRegistrationView,
    UserLoginView,
    UserProfileView,
    UserLogoutView,
    CustomTokenObtainPairView,
)
from users.views.auth import user_info, change_password

app_name = 'users'

urlpatterns = [
    # Registro
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('register/voluntario/', VoluntarioRegistrationView.as_view(), name='voluntario-register'),
    path('register/organizacao/', OrganizacaoRegistrationView.as_view(), name='organizacao-register'),
    
    # Autenticação
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    
    # JWT Tokens
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    
    # Perfil do usuário
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('info/', user_info, name='user-info'),
    path('change-password/', change_password, name='change-password'),
]