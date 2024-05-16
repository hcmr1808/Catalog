import pytest
import datetime
import time
from assertpy import assert_that
from GenreTestFixture import GenreTestFixture
from src.Domain.Entity.Genre import Genre
from src.Domain.Exceptions.EntityValidationException import EntityValidationException
import uuid

_genreTestFixture = GenreTestFixture()

def test_Instantiate():
    genreName = _genreTestFixture.GetValidGenreName()
    dateTimeBefore = datetime.datetime.now()
    genre = Genre(genreName)
    dateTimeAfter = datetime.datetime.now()

    assert genre is not None
    assert genre.id != ""
    assert dateTimeBefore <= genre.createdAt
    assert dateTimeAfter >= genre.createdAt
    assert genre.name == genreName
    assert genre.isActive == True

def test_InstantiateThrowWhenEmpty():
    with pytest.raises(EntityValidationException, match="Name should not be empty or null."):
        genre = Genre(None)

@pytest.mark.parametrize("isActive", [True, False])
def test_InstantiateWithIsActive(isActive:bool):
    genreName = _genreTestFixture.GetValidGenreName()
    dateTimeBefore = datetime.datetime.now()
    genre = Genre(genreName)
    dateTimeAfter = datetime.datetime.now()

    assert genre is not None
    assert genre.id != ""
    assert dateTimeBefore <= genre.createdAt
    assert dateTimeAfter >= genre.createdAt
    assert genre.name == genreName
    assert genre.isActive == True

@pytest.mark.parametrize("isActive", [True, False])
def test_Activate(isActive:bool):
    genre = _genreTestFixture.GetExampleGenre()
    oldName = genre.name

    genre.Activate()

    assert genre is not None
    assert genre.id != ""
    assert genre.isActive == True
    assert genre.name == oldName
    assert genre.createdAt is not None

@pytest.mark.parametrize("isActive", [True, False])
def test_Deactivate(isActive:bool):
    genre = _genreTestFixture.GetExampleGenre()
    oldName = genre.name

    genre.Deactivate()

    assert genre is not None
    assert genre.id != ""
    assert genre.isActive == False
    assert genre.name == oldName
    assert genre.createdAt is not None

def test_Update():
    genre = _genreTestFixture.GetExampleGenre()
    newName = _genreTestFixture.GetValidGenreName()
    oldIsActive = genre.isActive

    genre.Update(newName)

    assert genre is not None
    assert genre.id != ""
    assert genre.name == newName
    assert genre.isActive == oldIsActive
    assert genre.createdAt is not None
    
def test_UpdateThrowWhenNameEmpty():
    genre = _genreTestFixture.GetExampleGenre()
    
    with pytest.raises(EntityValidationException):
        genre.Update(None)

def test_AddCategory():
    genre = _genreTestFixture.GetExampleGenre()
    categoryUuid = str(uuid.uuid4())

    genre.AddCategory(categoryUuid)

    assert_that(genre.categories).is_length(1).contains(categoryUuid)

def test_AddTwoCategories():
    genre = _genreTestFixture.GetExampleGenre()
    categoryUuid1 = str(uuid.uuid4())
    categoryUuid2 = str(uuid.uuid4())

    genre.AddCategory(categoryUuid1)
    genre.AddCategory(categoryUuid2)

    assert len(genre.categories) == 2
    assert genre.categories[0] == categoryUuid1 and genre.categories[1] == categoryUuid2

def test_RemoveCategory():
    exampleUuid = uuid.uuid4()
    genre = _genreTestFixture.GetExampleGenre(
        categoriesIdsList=[uuid.uuid4(), uuid.uuid4(), exampleUuid, uuid.uuid4(), uuid.uuid4()]
    )
    genre.RemoveCategory(exampleUuid)

    assert len(genre.categories) == 4
    assert exampleUuid not in genre.categories
    
def test_RemoveAllCategories():
    genre = _genreTestFixture.GetExampleGenre(
        categoriesIdsList=[uuid.uuid4(), uuid.uuid4(), uuid.uuid4(), uuid.uuid4(), uuid.uuid4()]
    )

    genre.RemoveAllCategory()

    assert len(genre.categories) == 0

