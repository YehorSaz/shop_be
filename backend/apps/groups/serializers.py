from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.transaction import atomic
from rest_framework import serializers
from django.db.models import Q
from apps.courses.models import CourseModel
from apps.courses.serializers import CourseSerializer

from apps.groups.models import GroupModel
from apps.users.models import ProfileModel
from core.enums.regex_enum import RegExEnum

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = ('id', 'name', 'month', 'year', 'created_at', 'updated_at', 'modules', 'users')
        read_only_fields = ('id', 'created_at', 'updated_at', 'modules', 'users')

    def to_representation(self, instance):
        name = CourseSerializer(instance.name).data
        representation = super().to_representation(instance)
        representation |= {'name': name}
        return representation

    def create(self, validated_data):
        return GroupModel.objects.create_with_modules(validated_data)


class GroupUpdateModulesSerializer(CourseSerializer):
    class Meta:
        model = CourseModel
        fields = ('id', 'name', 'month', 'year', 'created_at', 'updated_at', 'modules')
        read_only_fields = ('id', 'name', 'month', 'year', 'created_at', 'updated_at')


class GroupAddUsersSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=50, validators=(
        RegexValidator(*RegExEnum.NAME_SURNAME.value),
    ))
    surname = serializers.CharField(max_length=50, validators=(
        RegexValidator(*RegExEnum.NAME_SURNAME.value),

    ))
    phone = serializers.CharField(max_length=12, validators=(
        RegexValidator(*RegExEnum.PHONE.value),
    ))

    def validate(self, attrs):
        print(attrs)
        email = attrs.get('email')
        phone = attrs.get('phone')
        exists = ProfileModel.objects.filter(phone=phone).filter(~Q(user__email=email)).exists()

        if exists:
            raise serializers.ValidationError({'details': f'{phone=} already registered'})

        return attrs

    @atomic()
    def create(self, validated_data):
        email = validated_data.pop('email')
        user, created = UserModel.objects.get_or_create_students_or_get_mentor(email=email)
        if created:
            ProfileModel.objects.create(**validated_data, user=user)
        user.groups.add(self.context['group'])
        return user
