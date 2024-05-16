from typing import Collection, List
from src.Domain.Validation.ValidationError import ValidationError
from src.Domain.Validation.ValidationHandler import ValidationHandler

class NotificationValidationHandler(ValidationHandler):
    def __init__(self):
        super().__init__()
        self._errors: List[ValidationError] = []
    
    @property
    def Errors(self) -> Collection[ValidationError]:
        return self._errors.copy()  

    def HasErrors(self) -> bool:
        return len(self._errors) > 0

    def HandleError(self, error: ValidationError):
        self._errors.append(error)
    