from django.contrib.auth import get_user_model

from rest_framework.generics import ListCreateAPIView

from core.permissions.is_superuser import IsSuperUser

from apps.admin.serializers import ManagerSerializer, MentorSerializer
from apps.users.models import UserModel as User

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
