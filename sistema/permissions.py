from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOrganizationAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.admin == request.user
    
class CanCreatePet(BasePermission):
    def has_permission(self, request, view):
        if request.method != "POST":
            return True

        model_name = view.queryset.model.__name__

        if model_name == "Perdidos":
            return request.user.is_authenticated

        if model_name == "Pet":
            return hasattr(request.user, "organization_admin") and request.user.organization_admin.exists()

        return False

    def has_object_permission(self, request, view, obj):
        if request.method != "POST":
            return True

        model_name = view.queryset.model.__name__

        if model_name == "Perdidos":
            return request.user.is_authenticated

        if model_name == "Pet":
            return hasattr(request.user, "organization_admin") and request.user.organization_admin.exists()

        return False