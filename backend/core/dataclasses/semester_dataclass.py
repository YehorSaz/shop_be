from dataclasses import dataclass

from core.dataclasses.base_dataclass import BaseDataClass


@dataclass
class Semester(BaseDataClass):
    name: str
    year: int
