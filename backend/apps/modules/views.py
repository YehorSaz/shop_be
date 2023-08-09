from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from drf_yasg.utils import swagger_auto_schema

from core.permissions.is_superuser import IsSuperUser

from apps.modules.models import ModuleModel
from apps.modules.serializers import ModuleResponseSerializer, ModuleSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(responses={200: ModuleResponseSerializer()}))
@method_decorator(name='post', decorator=swagger_auto_schema(responses={201: ModuleResponseSerializer()}))
class ModulesListCreateView(ListCreateAPIView):
    """
        get:
            List of modules
        post:
            Create new Module
    """
    serializer_class = ModuleSerializer
    queryset = ModuleModel.objects.all()
    permission_classes = (IsSuperUser,)


class ModuleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    pass  # todo release that
