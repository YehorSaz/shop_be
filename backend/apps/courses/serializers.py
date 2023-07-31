from rest_framework import serializers

from apps.courses.models import CourseModel, CourseNameModel


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseNameModel
        fields = ('id', 'name')


class CourseSerializer(serializers.ModelSerializer):
    name = CourseNameSerializer() # todo

    class Meta:
        model = CourseModel
        fields = ('id', 'name', 'month', 'year', 'created_at', 'updated_at', 'modules')
        read_only_fields = ('id', 'created_at', 'updated_at', 'modules')

    def create(self, validated_data):
        course: CourseModel = CourseModel.objects.create(**validated_data) # todo to service or managers
        last_course = CourseModel.objects.order_by('-id').filter(name_id=course.name).exclude(pk=course.pk).values('id')[
                      :1]
        if last_course:
            pk = last_course[0].get('id', None)
            if pk:
                modules = (CourseModel.objects.prefetch_related('modules')
                           .filter(pk=pk)
                           .values_list('modules', flat=True))
                course.modules.set(modules)
        return course
