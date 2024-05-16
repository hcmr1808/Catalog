import datetime
import time
import pytest
from src.Domain.Entity.Category import Category
from tests.UnitTests.Domain.Entity.Category.CategoryTestFixture import CategoryTestFixture
from src.Domain.Exceptions.EntityValidationException import EntityValidationException

categoryTestFixture = CategoryTestFixture()
                                    
def test_Instantiate():
    
    validCategory = categoryTestFixture.GetValidCategory()
    datetimeBefore = datetime.datetime.now()
    time.sleep(0.1)  
    category = Category(validCategory.name, validCategory.description)
    time.sleep(0.1) 
    datetimeAfter = datetime.datetime.now()

    assert category is not None
    assert category.name == validCategory.name
    assert category.description == validCategory.description
    assert category.id != ''  
    assert category.createdAt != datetime.datetime.min
    assert category.createdAt > datetimeBefore 
    assert category.createdAt < datetimeAfter 
    assert category.isActive is True 

def test_InstantiateErrorWhenNull():
    validCategory = categoryTestFixture.GetValidCategory()
    with pytest.raises(EntityValidationException, match="Name should not be empty or null."):
        category = Category(None, validCategory.description)

def test_InstantiateErrorWhenDescriptionIsNull():
    validCategory = categoryTestFixture.GetValidCategory()
    with pytest.raises(EntityValidationException, match="Description should not be null."):
        category = Category(validCategory.name, None)

@pytest.mark.parametrize("invalidName", ["a", "ab"])
def test_InstantiateErrorWhenNameLessThan3Characters(invalidName):
    validCategory = categoryTestFixture.GetValidCategory()
    with pytest.raises(EntityValidationException, match="Name should not be less than 3 characters."):
        category = Category(invalidName, validCategory.description)


def test_InstantiateErrorWhenNameGreaterThan255Characters():
    validCategory = categoryTestFixture.GetValidCategory()
    data = ['a' for _ in range(256)]
    invalidName = ''.join(data)
    with pytest.raises(EntityValidationException, match="Name should not be greater than 255 characters."):
        category = Category(invalidName, validCategory.description)

def test_IntanticErrorWhenDescriptionGreaterThan10000Characters():
    validCategory = categoryTestFixture.GetValidCategory()
    data = ['a' for _ in range(10001)]
    invalidDescription = ''.join(data)
    with pytest.raises(EntityValidationException, match="Description should not be greater than 10000 characters."):
        category = Category(validCategory.name, invalidDescription)

def test_Activate():
    validCategory = categoryTestFixture.GetValidCategory()
    category = Category(validCategory.name, validCategory.description, False)
    category.Activate()
    assert category.isActive == True

def test_Deactivate():
    validCategory = categoryTestFixture.GetValidCategory()
    category = Category(validCategory.name, validCategory.description, True)
    category.Deactivate()
    assert category.isActive == False

def test_Update():
    validCategory = categoryTestFixture.GetValidCategory()
    newValidCategory = categoryTestFixture.GetValidCategory()
    
    category = Category(validCategory.name, validCategory.description)
    category.Update(newValidCategory.name, newValidCategory.description)

    assert newValidCategory.name == category.name
    assert newValidCategory.description == category.description

def test_UpdateOnlyName():
    validCategory = categoryTestFixture.GetValidCategory()
    newValidCategory = categoryTestFixture.GetValidCategory()
    category = Category(validCategory.name, validCategory.description)
    currentDescription = category.description
    category.Update(newValidCategory.name)
    assert newValidCategory.name == category.name
    assert category.description == currentDescription

def test_UpdateErrorWhenNameEmpty():
    validCategory = categoryTestFixture.GetValidCategory()
    newValidCategory = categoryTestFixture.GetValidCategory()
    category = Category(validCategory.name, validCategory.description)

    with pytest.raises(EntityValidationException, match="Name should not be empty or null."):    
        category.Update(None, newValidCategory.description)

@pytest.mark.parametrize("invalidName", ["a", "ab"])
def test_UpdateErrorWhenNameLessThan3Characters(invalidName):
    validCategory = categoryTestFixture.GetValidCategory()
    newValidCategory = categoryTestFixture.GetValidCategory()
    category = Category(validCategory.name, validCategory.description)
    with pytest.raises(EntityValidationException, match="Name should not be less than 3 characters."):    
        category.Update(invalidName, newValidCategory.description)

def test_UpdateErrorWhenNameGreaterThan255Characters():
    validCategory = categoryTestFixture.GetValidCategory()
    category = Category(validCategory.name, validCategory.description)
    data = ['a' for _ in range(256)]
    invalidName = ''.join(data)
    with pytest.raises(EntityValidationException, match="Name should not be greater than 255 characters."):
        category.Update(invalidName)

def test_UpdateErrorWhenDescriptionGreaterThan10000Characters():
    validCategory = categoryTestFixture.GetValidCategory()
    category = Category(validCategory.name, validCategory.description)
    newValidCategory = categoryTestFixture.GetValidCategory()
    data = ['a' for _ in range(10001)]
    invalidDescription = ''.join(data)
    with pytest.raises(EntityValidationException, match="Description should not be greater than 10000 characters."):
        category.Update(newValidCategory.name, invalidDescription)