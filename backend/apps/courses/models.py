from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from apps.courses.choices.month_choices import MonthChoices
from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class CourseNameModel(BaseModel):
    class Meta:
        db_table = 'course_names'

    name = models.CharField(max_length=20, unique=True, validators=(
        RegexValidator(*RegExEnum.COURSE_NAME.value),
    ))


class CourseModel(BaseModel):
    class Meta:
        db_table = 'courses'
        ordering = ('-id',)
        unique_together = ('name', 'month', 'year')

    name = models.ForeignKey(CourseNameModel, on_delete=models.CASCADE, related_name='courses')
    month = models.CharField(max_length=3, choices=MonthChoices.choices)
    year = models.IntegerField(validators=(
        MinValueValidator(datetime.now().year),
        MaxValueValidator(datetime.now().year + 1),
    ))
    users = models.ManyToManyField(UserModel, related_name='courses')
