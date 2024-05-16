from abc import ABC, abstractmethod
from src.Domain.Validation.ValidationHandler import ValidationHandler

class Validator(ABC):
    def __init__(self, handler: ValidationHandler):
        self._handler = handler

    @abstractmethod
    def Validate(self):
        pass
