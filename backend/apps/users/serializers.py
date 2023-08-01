from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from core.dataclasses.user_dataclass import User as UserDataclass

from apps.users.choices.role_choice import RoleChoice
from apps.users.models import ProfileModel
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'phone', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'is_active', 'last_login', 'created_at', 'updated_at', 'profile',)
        read_only_fields = ('id', 'is_active', 'last_login', 'created_at', 'updated_at',)

    def to_representation(self, instance: UserDataclass):
        role = 'user'
        match instance:
            case User(is_superuser=True):
                role = 'superuser'
            case User(is_manager=True):
                role = 'manager'
            case User(is_staff=True):
                role = 'mentor'

        representation = super().to_representation(instance)
        representation |= {'role': role}
        return representation

    @atomic()
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user


class UserResponseSerializer(UserSerializer):
    role = serializers.ChoiceField(choices=RoleChoice)

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'is_active', 'role', 'last_login', 'created_at', 'updated_at', 'profile',)


class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('password',)
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
