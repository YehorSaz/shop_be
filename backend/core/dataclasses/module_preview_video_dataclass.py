from dataclasses import dataclass

from core.dataclasses.base_dataclass import BaseDataClass
from core.dataclasses.module_dataclass import Module


@dataclass
class ModulePreviewVideo(BaseDataClass):
    link: str
    module: Module
