from django.core.validators import RegexValidator
from django.db import models

from apps.groups.models import GroupModel
from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

# from apps.courses.models import CourseModel


class ModuleModel(BaseModel):
    class Meta:
        db_table = 'modules'

    name = models.CharField(max_length=11, unique=True, validators=(
        RegexValidator(*RegExEnum.MODULE_NAME.value),
    ))
    preview_playlist = models.URLField(max_length=255, blank=True)
    groups = models.ManyToManyField(GroupModel, related_name='modules')
