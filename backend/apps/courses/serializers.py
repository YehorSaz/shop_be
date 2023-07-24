from rest_framework import serializers

from .models import CourseModel, CourseSemesterModel


class CourseSemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSemesterModel
        fields = ('id', 'name', 'year')


class CourseSerializer(serializers.ModelSerializer):
    semester = CourseSemesterSerializer()

    class Meta:
        model = CourseModel
        fields = ('id', 'name', 'semester')
