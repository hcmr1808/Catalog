from faker import Faker
from src.Domain.Entity.CastMember import CastMember
from src.Domain.Validation.DomainValidation import DomainValidation
import random

class CastMemberTestFixture:
    def __init__(self):
        self.fake = Faker()

    def GetValidCastMemberName(self):
        castMember = self.fake.name()
        return castMember

    def GetValidCastMemberType(self):
        type_list = ['ACTOR', 'DIRECTOR']
        castMemberType = random.choice(type_list)
        return castMemberType
    
    def GetValidCastMember(self):
        valid_name = self.GetValidCastMemberName()
        valid_type = self.GetValidCastMemberType()
        return CastMember(valid_name, valid_type)


