from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class ManagerSerializer(UserSerializer):
    @atomic()
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        manager = UserModel.objects.create_manager(**validated_data)
        ProfileModel.objects.create(**profile, user=manager)
        return manager


class MentorSerializer(UserSerializer):
    @atomic()
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        mentor = UserModel.objects.create_mentor(**validated_data)
        ProfileModel.objects.create(**profile, user=mentor)
        return mentor
