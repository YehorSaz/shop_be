from django.db import models


class MonthChoices(models.TextChoices):
    Jan = 'Jan'
    Feb = 'Feb'
    Mar = 'Mar'
    Apr = 'Apr'
    May = 'May'
    Jun = 'Jun'
    Jul = 'Jul'
    Aug = 'Aug'
    Sep = 'Sep'
    Oct = 'Oct'
    Nov = 'Nov'
    Dec = 'Dec'
