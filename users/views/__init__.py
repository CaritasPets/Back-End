from .user import (
    UserRegistrationView,
    UserProfileView,
)
from .auth import (
    CustomTokenObtainPairView,
    LoginView,
    LogoutView
)
__all__ = [
    'UserRegistrationView',
    'LoginView',
    'UserProfileView',
    'LogoutView',
    'CustomTokenObtainPairView',
]