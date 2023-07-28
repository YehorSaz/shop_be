from rest_framework.generics import ListCreateAPIView

from core.permissions.is_superuser import IsSuperUser

from apps.modules.models import ModuleModel
from apps.modules.serializers import ModuleSerializer


class ModulesListCreateView(ListCreateAPIView):
    serializer_class = ModuleSerializer
    queryset = ModuleModel.objects.all()
    permission_classes = (IsSuperUser,)
