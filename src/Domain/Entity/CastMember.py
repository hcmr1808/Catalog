import datetime
from src.Domain.Validation.DomainValidation import DomainValidation
from src.Domain.SeedWork.AggregateRoot import AggregateRoot
from src.Domain.Enum.CastMemberType import CastMemberType

class CastMember(AggregateRoot):
    def __init__(self, name, castType:CastMemberType):
        super().__init__()
        self.name = name
        self.castType = castType
        createdAt = datetime.datetime.now()
        self.Validate()
    
    def Update(self, name, castType):
        self.name = name
        self.castType = castType
        self.Validate()
    
    def Validate(self):
        DomainValidation.NotNullOrEmpty(self.name, "Name")

    def __str__(self):
        return f'[Id] = {self.id}, [Name] = {self.name}, [CreatedAt] = {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
    