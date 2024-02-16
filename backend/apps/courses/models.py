from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class CourseModel(BaseModel):
    class Meta:
        db_table = 'course'

    name = models.CharField(max_length=20, unique=True, validators=(
        RegexValidator(*RegExEnum.COURSE_NAME.value),
    ))
