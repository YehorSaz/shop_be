import os

from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from apps.users.models import ProfileModel
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

UserModel: User = get_user_model()


class ManagerSerializer(UserSerializer):
    @atomic()
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_superuser(is_active=False, **validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user


class ManagerActivationRecoveryPasswordRequestResponseSerializer(serializers.Serializer):
    url = serializers.CharField(default=f'{os.environ.get("FRONTEND")}/auth/activate/<token>')
