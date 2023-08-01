from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView

from drf_yasg.utils import swagger_auto_schema

from core.permissions.is_superuser import IsSuperUser

from apps.admin.serializers import ManagerSerializer, MentorSerializer
from apps.users.models import UserModel as User
from apps.users.serializers import UserResponseSerializer

UserModel: User = get_user_model()


@method_decorator(name='get', decorator=swagger_auto_schema(responses={200: UserResponseSerializer()}))
@method_decorator(name='post', decorator=swagger_auto_schema(responses={201: UserResponseSerializer()}))
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


@method_decorator(name='get', decorator=swagger_auto_schema(responses={200: UserResponseSerializer()}))
@method_decorator(name='post', decorator=swagger_auto_schema(responses={201: UserResponseSerializer()}))
class MentorListCreateView(ListCreateAPIView):
    """
    get:
        Get List of mentors
    post:
        Create Mentor
    """
    serializer_class = MentorSerializer
    queryset = UserModel.objects.mentors()
    permission_classes = (IsSuperUser,)
