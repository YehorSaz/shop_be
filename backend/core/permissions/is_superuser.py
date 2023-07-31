import os

from rest_framework.request import Request

from core.permissions.is_manager import IsManager


class IsSuperUser(IsManager):
    def has_permission(self, request: Request, view) -> bool:
        return super().has_permission(request, view) and request.user.is_superuser
