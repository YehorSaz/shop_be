from dataclasses import dataclass

from .base_dataclass import BaseDataClass


@dataclass
class Profile(BaseDataClass):
    id = int
    name = str
    surname = str
    phone = str
