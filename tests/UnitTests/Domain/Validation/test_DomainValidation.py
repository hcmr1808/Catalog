import random
import pytest
from faker import Faker
from src.Domain.Exceptions.EntityValidationException import EntityValidationException
from src.Domain.Validation.DomainValidation import DomainValidation

faker = Faker()

def test_NotNullOk():
    value = faker.name()  
    field_name = faker.name().replace(" ", "")  
    print(value, field_name)
    
    assert DomainValidation.NotNull(value, field_name) is None

def test_NotNullThrowWhenNull():
    with pytest.raises(EntityValidationException):
        DomainValidation.NotNull(None, "KentRogers")

def test_NotNullOrEmptyOk():
    value = faker.name()
    field_name = faker.name().replace(" ", "")
    
    assert DomainValidation.NotNullOrEmpty(value, field_name) is None

def test_NotNullOrEmptyThrowWhenEmpty():
    field_name = faker.name().replace(" ", "")
    with pytest.raises(EntityValidationException):
        DomainValidation.NotNullOrEmpty("", field_name)

def test_MinLengthOk():
    value = faker.name()
    field_name = faker.name().replace(" ", "")
    minLength = 3

    assert DomainValidation.MinLength(value, minLength, field_name) is None

def test_MinLengthThrowWhenLess():
    value = faker.name()
    shortened_value = value[:2]
    field_name = faker.name().replace(" ", "")
    minLength = 3

    with pytest.raises(EntityValidationException):
        DomainValidation.MinLength(shortened_value, minLength, field_name)

def test_MaxLengthOk():
    value = faker.name()
    maxLength = 1000
    field_name = faker.name()

    assert DomainValidation.MaxLength(value, maxLength, field_name) is None

def test_MaxLengthThrowWhenGreater():
    data = ['a' for _ in range(10001)]
    value = ''.join(data)
    field_name = faker.name().replace(" ", "")
    maxLength = 1000

    with pytest.raises(EntityValidationException):
        DomainValidation.MaxLength(value, maxLength, field_name)