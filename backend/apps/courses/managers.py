from django.db.models import Manager
from django.db.transaction import atomic


class CourseManager(Manager):

    @atomic()
    def create_with_modules(self, validated_data):
        """
            Create course and add modules from last course
        """
        course = self.create(**validated_data)
        last_course = self.order_by('-id').filter(name_id=course.name).exclude(pk=course.pk).values('id')[:1]
        if last_course:
            pk = last_course[0].get('id', None)
            if pk:
                modules = self.prefetch_related('modules').filter(pk=pk).values_list('modules', flat=True)
                modules = [module for module in modules if module]
                if modules:
                    course.modules.set(modules)
        return course

    def all_with_users(self):
        return self.prefetch_related('users').all()
