from dataclasses import dataclass
from datetime import datetime

from core.dataclasses.base_dataclass import BaseDataClass
from core.dataclasses.profile_dataclass import Profile


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
