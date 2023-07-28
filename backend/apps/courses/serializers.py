from django.db.transaction import atomic

from rest_framework import serializers

from apps.courses.models import CourseModel, CourseSemesterModel


class CourseSemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSemesterModel
        fields = ('id', 'name', 'year', 'created_at', 'updated_at')


class CourseSerializer(serializers.ModelSerializer):
    semester = CourseSemesterSerializer()

    class Meta:
        model = CourseModel
        fields = ('id', 'name', 'semester', 'created_at', 'updated_at')

    @atomic()
    def create(self, validated_data):
        semester = validated_data.pop('semester')
        semester = CourseSemesterModel.objects.create(**semester)
        course = CourseModel.objects.create(semester=semester,**validated_data)
        return course
