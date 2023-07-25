from django.core.validators import RegexValidator
from django.db import models

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from apps.courses.models import CourseModel


class ModuleModel(BaseModel):
    class Meta:
        db_table = 'modules'

    name = models.CharField(max_length=10, validators=(
        RegexValidator(*RegExEnum.COURSE_NAME.value),
    ))
    courses = models.ManyToManyField(CourseModel)


class ModulePreviewVideosModel(BaseModel):
    class Meta:
        db_table = 'module_preview_videos'

    link = models.URLField(max_length=255)
    module = models.ForeignKey(ModuleModel, on_delete=models.CASCADE, related_name='preview')


