from dataclasses import dataclass

from core.dataclasses.base_dataclass import BaseDataClass
from core.dataclasses.module_dataclass import Module
from core.dataclasses.semester_dataclass import Semester
from core.dataclasses.user_dataclass import User


@dataclass
class Course(BaseDataClass):
    name: str
    semester: Semester
    users: list[User]
    modules: list[Module]
