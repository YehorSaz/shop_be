from dataclasses import dataclass
from datetime import datetime

from .base_dataclass import BaseDataClass
from .profile_dataclass import Profile


@dataclass
class User(BaseDataClass):
    id = int
    email = str
    password = str
    is_active = bool
    is_staff = bool
    is_superuser = bool
    last_login = datetime
    profile = Profile
