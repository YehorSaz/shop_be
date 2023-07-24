from rest_framework import serializers

from .models import CourseModel, SemesterModel


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterModel
        fields = ('id', 'name', 'year')


class CourseSerializer(serializers.ModelSerializer):
    semester = SemesterSerializer()

    class Meta:
        model = CourseModel
        fields = ('id', 'name', 'semester')
