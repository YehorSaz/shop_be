from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from apps.users.managers import CustomUserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=(
        RegexValidator(*RegExEnum.PASSWORD.value),
    ))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    # todo add is_manager
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=50, validators=(
        RegexValidator(*RegExEnum.NAME_SURNAME.value),
    ))
    surname = models.CharField(max_length=50, validators=(
        RegexValidator(*RegExEnum.NAME_SURNAME.value),

    ))
    phone = models.CharField(max_length=12, unique=True, validators=(
        RegexValidator(*RegExEnum.PHONE.value),
    ))
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
