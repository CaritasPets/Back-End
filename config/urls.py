from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

from sistema.views import OrganizacaoViewSet, PetViewSet, PerdidosViewSet
from uploader.views import ImageUploadViewSet, DocumentUploadViewSet

router.register(r"organizacoes", OrganizacaoViewSet)
router.register(r"pets", PetViewSet)
router.register(r"perdidos", PerdidosViewSet)
router.register(r"images", ImageUploadViewSet)
router.register(r"documents", DocumentUploadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path("api/media/", include(uploader_router.urls)),
]