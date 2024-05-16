import datetime
from typing import Optional
from src.Domain.Validation.DomainValidation import DomainValidation
from src.Domain.SeedWork.Entity import Entity
from src.Domain.SeedWork.AggregateRoot import AggregateRoot

class Category(AggregateRoot):
    def __init__(self, name:str, description:str, isActive:bool=True):
        super().__init__()
        self.name = name
        self.description = description
        self.createdAt = datetime.datetime.now()
        self.isActive = isActive
        self.Validate()
    
    def Update(self, name, description: Optional[str] = None):
        self.name = name
        if description is not None:
            self.description = description
        self.Validate()

    def Deactivate(self):
        self.isActive = False
        self.Validate()

    def Activate(self):
        self.isActive = True
        self.Validate()

    def Validate(self):
        DomainValidation.NotNullOrEmpty(self.name, "Name")
        DomainValidation.MaxLength(self.name, 255, "Name")
        DomainValidation.MinLength(self.name, 3, "Name")

        DomainValidation.NotNull(self.description, "Description")
        DomainValidation.MaxLength(self.description, 10000, "Description")

    