from rest_framework import serializers

from apps.courses.models import CourseModel, CourseNameModel


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseNameModel
        fields = ('id', 'name')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ('id', 'name', 'month', 'year', 'created_at', 'updated_at', 'modules')
        read_only_fields = ('id', 'created_at', 'updated_at', 'modules')

    def to_representation(self, instance):
        name = CourseNameSerializer(instance.name).data
        representation = super().to_representation(instance)
        representation |= {'name': name}
        return representation

    def create(self, validated_data):
        return CourseModel.objects.create_with_modules(validated_data)
