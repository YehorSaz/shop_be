from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsSuperUserOrManagerReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and request.user.is_manager or
            request.user and
            request.user.is_superuser
        )
