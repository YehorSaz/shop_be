import os

from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as TRView

from core.permissions.is_superuser import IsSuperUser
from core.services.jwt_service import JWTService
from core.tokens.activate_token import ActivateToken

from apps.auth.serializers import UserActivationResponseSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserPasswordSerializer, UserResponseSerializer

UserModel: User = get_user_model()


class MeView(RetrieveAPIView):
    """
        Return Authenticated User
    """
    serializer_class = UserResponseSerializer

    def get_object(self):
        return self.request.user


@method_decorator(name='post', decorator=swagger_auto_schema(responses={201: TokenRefreshSerializer()}, security=[]))
class TokenPairView(TokenObtainPairView):
    """
        Login
    """
    pass


@method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class TokenRefreshView(TRView):
    """
        Refresh tokens
    """
    pass


class UserActivateView(GenericAPIView):
    """
    User activation and set password by token
    """
    permission_classes = (AllowAny,)
    serializer_class = UserPasswordSerializer

    @swagger_auto_schema(security=[], responses={'200': UserResponseSerializer()})
    def patch(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user: User = JWTService.validate_token(token, ActivateToken)
        user.set_password(data['password'])

        if not user.is_active:
            user.is_active = True

        user.save()
        res_serializer = UserResponseSerializer(user)
        return Response(res_serializer.data, status=status.HTTP_200_OK)



class UserActivationRequestView(GenericAPIView):
    """
    Request for activation
    """
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()
    pagination_class = None

    def get_serializer(self, *args, **kwargs):
        pass

    @swagger_auto_schema(responses={'200': UserActivationResponseSerializer()})
    def get(self, *args, **kwargs):
        user = self.get_object()
        token = JWTService.create_token(user, ActivateToken)
        url = f'{os.environ.get("FRONTEND")}/auth/activate/{token}'
        return Response({'url': url}, status.HTTP_200_OK)
