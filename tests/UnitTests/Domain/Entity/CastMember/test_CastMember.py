import pytest
from CastMemberFixture import CastMemberTestFixture
from src.Domain.Entity.CastMember import CastMember
from src.Domain.Exceptions.EntityValidationException import EntityValidationException

castMemberFixture = CastMemberTestFixture()

def test_Instantiate():
    valid_castMember = castMemberFixture.GetValidCastMember()
    member = CastMember(valid_castMember.name, valid_castMember.castType)
    assert member is not None
    assert member.id != ''

def test_InstantiateWhenNameEmpty():
    valid_castMember = castMemberFixture.GetValidCastMember()
    with pytest.raises(EntityValidationException, match="Name should not be empty or null."):
        member = CastMember(None, valid_castMember.castType)

def test_Update():
    valid_castMember = castMemberFixture.GetValidCastMember()
    member = CastMember(valid_castMember.name, valid_castMember.castType)
    newValid_castMember = castMemberFixture.GetValidCastMember()
    member.Update(newValid_castMember.name, newValid_castMember.castType)

    assert newValid_castMember.name == member.name
    assert newValid_castMember.castType == member.castType