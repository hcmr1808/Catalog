from src.Domain.SeedWork.ValueObjects import ValueObject
from typing import Union

class Image(ValueObject):
    def __init__(self, path: str):
        self.path = path

    def __eq__(self, other: Union['Image', ValueObject]) -> bool:
        if not isinstance(other, Image):
            return False
        return self.path == other.path

    def __hash__(self) -> int:
        return hash(self.path)

    def __repr__(self) -> str:
        return f"Image(path={self.path})"
    