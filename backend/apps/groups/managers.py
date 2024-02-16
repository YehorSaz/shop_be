from django.db.models import Manager
from django.db.transaction import atomic


class GroupManager(Manager):

    @atomic()
    def create_with_modules(self, validated_data):
        """
            Create group and add modules from last group
        """
        group = self.create(**validated_data)
        last_group = self.order_by('-id').filter(name_id=group.name).exclude(pk=group.pk).values('id')[:1]
        if last_group:
            pk = last_group[0].get('id', None)
            if pk:
                modules = self.prefetch_related('modules').filter(pk=pk).values_list('modules', flat=True)
                modules = [module for module in modules if module]
                if modules:
                    group.modules.set(modules)
        return group

    def all_with_users(self):
        return self.prefetch_related('users').all()
