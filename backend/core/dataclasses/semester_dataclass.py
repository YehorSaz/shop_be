from dataclasses import dataclass

from .base_dataclass import BaseDataClass


@dataclass
class Semester(BaseDataClass):
    name: str
    year: int
