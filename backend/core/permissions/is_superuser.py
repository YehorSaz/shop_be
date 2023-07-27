import os

from rest_framework.request import Request

from .is_manager import IsManager


class IsSuperUser(IsManager):
    def has_permission(self, request: Request, view) -> bool:
        return (super().has_permission(request, view)
                and request.user.email in os.environ.get('SUPERUSERS', '').split(','))
