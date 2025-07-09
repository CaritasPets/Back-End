from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

from sistema.views import OrganizacaoViewSet, PetViewSet, PerdidosViewSet, PorteViewSet, RacaViewSet, UsuarioViewSet, VoluntarioViewSet

router.register(r"organizacoes", OrganizacaoViewSet)
router.register(r"pets", PetViewSet)
router.register(r"perdidos", PerdidosViewSet)
router.register(r"portes", PorteViewSet)
router.register(r"racas", RacaViewSet)
router.register(r"usuario", UsuarioViewSet)
router.register(r"voluntarios", VoluntarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/media/", include(uploader_router.urls)),
    path('api/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)