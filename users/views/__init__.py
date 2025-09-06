from .user import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    UserLogoutView,
)
from .auth import CustomTokenObtainPairView
__all__ = [
    'UserRegistrationView',
    'UserLoginView',
    'UserProfileView',
    'UserLogoutView',
    'CustomTokenObtainPairView',
]