from src.Domain.SeedWork.AggregateRoot import AggregateRoot
import datetime
from typing import List
import uuid
from src.Domain.Validation.DomainValidation import DomainValidation

class Genre(AggregateRoot):
    def __init__(self, name:str, isActive:bool = True):
        super().__init__()
        self.name = name
        self.isActive = isActive
        self.createdAt = datetime.datetime.now()
        self._categories = []
        self.Validate()
    
    @property
    def categories(self)-> List[uuid.UUID]:
        return self._categories[:]
    
    def Deactivate(self):
        self.isActive = False
        self.Validate()

    def Activate(self):
        self.isActive = True
        self.Validate()

    def Update(self, name):
        self.name = name
        self.Validate()

    def AddCategory(self, category_id: uuid.UUID):
        self._categories.append(category_id)
        self.Validate()
    
    def RemoveCategory(self, category_id: uuid.UUID):
        try:
            self._categories.remove(category_id)
        except ValueError:
            raise ValueError("UUID not found in categories list")
        self.Validate()

    
    def RemoveAllCategory(self):
        self._categories = []
        self.Validate()
    
    def Validate(self):
        DomainValidation.NotNullOrEmpty(self.name, "Name")


