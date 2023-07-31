from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request


class IsManager(IsAdminUser):
    def has_permission(self, request: Request, view) -> bool:
        return super().has_permission(request, view) and request.user.is_manager
