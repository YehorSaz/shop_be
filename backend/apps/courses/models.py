from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from apps.users.models import UserModel as User

from .choices.semester_choices import SemesterChoices

UserModel: User = get_user_model()

class CourseSemesterModel(BaseModel):
    class Meta:
        db_table = 'course_semesters'

    name = models.CharField(max_length=3, choices=SemesterChoices.choices)
    year = models.IntegerField(validators=(
        MinValueValidator(datetime.now().year),
        MaxValueValidator(datetime.now().year + 1),
    ))


class CourseModel(BaseModel):
    class Meta:
        db_table = 'courses'

    name = models.CharField(max_length=20, validators=(
        RegexValidator(RegExEnum.COURSE_NAME.pattern, RegExEnum.COURSE_NAME.msg),
    ))
    semester = models.OneToOneField(CourseSemesterModel, on_delete=models.CASCADE, related_name='course')
    users = models.ManyToManyField(UserModel)
