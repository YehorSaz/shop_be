from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView as TRView

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

from .serializers import UserResponseSerializer

UserModel: User = get_user_model()


@method_decorator(name='post', decorator=swagger_auto_schema(responses={201: UserResponseSerializer()}, security=[]))
class RegisterView(CreateAPIView):
    """
        Register User
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


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
