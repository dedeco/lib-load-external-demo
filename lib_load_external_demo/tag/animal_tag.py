from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict

from lib_load_external_demo.tag.tag import Tag, Info


class SampleEnum(Enum):
    NOT_INFORMED = "NOT_INFORMED"
    PUBLIC = "PUBLIC"
    CONFIDENTIAL = "CONFIDENTIAL"


@dataclass
class AnimalTag(Tag):
    """Class for Animal tag information

    Attributes:
        name (str): sample name to be loaded
        foo (bool): just a True or False
        bar (float): some float
        baz (enum): PUBLIC or CONFIDENTIAL
    """

    name: str
    baz: SampleEnum
    foo: Optional[bool] = None
    bar: Optional[float] = 0

    _display_name: str = "Animal"
    _tag_id: str = "animal"
    _is_publicly_readable: bool = True

    def as_dict(self) -> Dict[str, Info]:
        return {
            "name": {"value": self.name, "display_name": "name", "description": "name"},
            "foo": {"value": self.foo, "display_name": "foo name", "description": "foo description"},
            "bar": {"value": self.bar, "display_name": "bar name", "description": "bar description"},
            "baz": {"value": self.baz.value, "display_name": "baz name", "description": "baz description"}
        }
