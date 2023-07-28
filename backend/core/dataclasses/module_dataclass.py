from dataclasses import dataclass

from core.dataclasses.base_dataclass import BaseDataClass
from core.dataclasses.course_dataclass import Course


@dataclass
class Module(BaseDataClass):
    name: str
    courses: list[Course]
