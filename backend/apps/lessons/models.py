from django.db import models

from core.models import BaseModel

from apps.modules.models import ModuleModel


class LessonModel(BaseModel):
    class Meta:
        db_table = 'lessons'

    description = models.CharField(max_length=255)
    module = models.ForeignKey(ModuleModel, on_delete=models.CASCADE, related_name='lessons')


class LessonVideosModel(BaseModel):
    class Meta:
        db_table = 'lesson_videos'

    link = models.URLField(max_length=255)
    lesson = models.ForeignKey(LessonModel, on_delete=models.CASCADE, related_name='videos')


