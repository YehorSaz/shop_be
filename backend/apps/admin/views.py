import os

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.permissions.is_superuser import IsSuperUser
from core.services.jwt_service import JWTService
from core.tokens.activate_token import ActivateToken

from apps.users.models import UserModel as User

from ..users.serializers import UserPasswordSerializer, UserResponseSerializer
from .serializers import ManagerActivationRecoveryPasswordRequestResponseSerializer, ManagerSerializer

UserModel: User = get_user_model()


class ManagerListCreateView(ListCreateAPIView):
    """
    get:
        Get list of managers
    post:
        Create manager
    """
    serializer_class = ManagerSerializer
    queryset = UserModel.objects.managers()
    permission_classes = (IsSuperUser,)


class ManagerActivationRecoveryPasswordRequestView(GenericAPIView):
    """
    Request for activation or recovery password
    """
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.managers()
    pagination_class = None

    def get_serializer(self, *args, **kwargs):
        pass

    @swagger_auto_schema(responses={'200': ManagerActivationRecoveryPasswordRequestResponseSerializer()})
    def get(self, *args, **kwargs):
        manager = self.get_object()
        token = JWTService.create_token(manager, ActivateToken)
        url = f'{os.environ.get("FRONTEND")}/auth/activate/{token}'
        return Response({'url': url}, status.HTTP_200_OK)


class ManagerActivateRecoveryPasswordView(GenericAPIView):
    """
    Manager activation  and set password by token
    """
    permission_classes = (AllowAny,)
    serializer_class = UserPasswordSerializer

    @swagger_auto_schema(security=[], responses={'200': UserResponseSerializer()})
    def patch(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        manager: User = JWTService.validate_token(token, ActivateToken)
        manager.set_password(data['password'])

        if not manager.is_active:
            manager.is_active = True

        manager.save()
        res_serializer = UserResponseSerializer(manager)
        return Response(res_serializer.data, status=status.HTTP_200_OK)
