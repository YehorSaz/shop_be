from django.db.models import TextChoices


class RoleChoice(TextChoices):
    USER = 'user',
    MENTOR = 'mentor'
    MANAGER = 'manager'
    SUPERUSER = 'superuser'

