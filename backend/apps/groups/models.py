from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.courses.choices.month_choices import MonthChoices
from apps.courses.models import CourseModel
from apps.groups.managers import GroupManager
from apps.users.models import UserModel as User
from core.models import BaseModel

UserModel: User = get_user_model()


class GroupModel(BaseModel):
    class Meta:
        db_table = 'groups'
        ordering = ('-id',)
        unique_together = ('name', 'month', 'year')

    name = models.ForeignKey(CourseModel, on_delete=models.CASCADE, related_name='group')
    month = models.CharField(max_length=3, choices=MonthChoices.choices)
    year = models.IntegerField(validators=(
        MinValueValidator(datetime.now().year),
        MaxValueValidator(datetime.now().year + 1),
    ))
    users = models.ManyToManyField(UserModel, related_name='group')

    objects = GroupManager()
