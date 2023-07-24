from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.enums.regex_enum import RegExEnum
from core.models import BaseModel

from .managers import CustomUserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(_("password"), max_length=128, validators=(
        RegexValidator(RegExEnum.PASSWORD.pattern, RegExEnum.PASSWORD.msg),
    ))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=50, validators=(
        RegexValidator(RegExEnum.NAME_SURNAME.pattern, RegExEnum.NAME_SURNAME.msg),
    ))
    surname = models.CharField(max_length=50, validators=(
        RegexValidator(RegExEnum.NAME_SURNAME.pattern, RegExEnum.NAME_SURNAME.msg),

    ))
    phone = models.CharField(max_length=12, validators=(
        RegexValidator(RegExEnum.PHONE.pattern, RegExEnum.PHONE.msg),
    ))
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
