from dataclasses import dataclass

from .base_dataclass import BaseDataClass
from .semester_dataclass import Semester


@dataclass
class Course(BaseDataClass):
    name: str
    semester: Semester
