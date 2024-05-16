from abc import ABC
from src.Domain.Validation.ValidationError import ValidationError


class ValidationHandler(ABC):
    def HandleError(message):
        ValidationError(message)

    

