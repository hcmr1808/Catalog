from typing import override
from src.Domain.Validation.ValidationHandler import ValidationHandler
from src.Domain.Validation.Validator import Validator

class VideoValidator(Validator):
    def __init__(self, video, handler: ValidationHandler):
        super().__init__(handler)
        self.video = video
        self.titleMaxLength:int = 255
        self.descriptionMaxLength:int = 4000

    @override
    def Validate(self):
        self.ValidateTitle()
 
        if not self.video.description:
            self._handler.HandleError("Description is required")

        description = self.video.description

        if len(str(description)) > 4000:  
            self._handler.HandleError(f"Description should be less or equal {self.descriptionMaxLength} characters long")

    def ValidateTitle(self):
        
        if not self.video.title:
            self._handler.HandleError("Title is required")
        

        if len(str(self.video.title)) > 255:  
            self._handler.HandleError(f"Title should be less or equal {self.titleMaxLength} characters long")


    
