from django.contrib.auth import get_user_model

from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class UserResponseSerializer(UserSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created', 'updated', 'profile',
        )
