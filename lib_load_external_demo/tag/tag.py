from typing import TypedDict, Any


class Info(TypedDict):
    value: Any
    display_name: str
    description: str


class Tag:
    """Class for Tag abstraction

        When created attributes in child class follow these steps:
            For optional fields declare using Optional and set default as None or 0 (for float)
                foo: Optional[str] = None
                baz: Optional[bool] = None
            For required fields use:
                bar: bool

        Override _display_name and _is_publicly_readable in child dataclass

        Override as_dict method follow docs strings actions. The order of fields will be used
        to create the tag template

    """

    _display_name: str = "Tag"
    _tag_id: str = None
    _is_publicly_readable: bool = True

    def get_tag_id(self) -> str:
        return self._tag_id
