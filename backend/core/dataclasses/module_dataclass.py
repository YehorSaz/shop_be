from dataclasses import dataclass

from core.dataclasses.base_dataclass import BaseDataClass


@dataclass
class Module(BaseDataClass):
    name: str
    preview_playlist: str
