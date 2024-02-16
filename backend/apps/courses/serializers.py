from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.courses.models import CourseModel
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ('id', 'name')
