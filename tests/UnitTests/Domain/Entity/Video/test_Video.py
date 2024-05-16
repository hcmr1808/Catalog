from typing import List
import uuid
from src.Domain.Entity.Video import Video
from src.Domain.Exceptions.EntityValidationException import EntityValidationException
from src.Domain.Validation.NotificationValidationHandler import NotificationValidationHandler
from src.Domain.Validation.ValidationError import ValidationError
from tests.UnitTests.Domain.Entity.Video.VideoTestFixture import VideoTestFixture
from datetime import datetime, timedelta
from assertpy import assert_that
from src.Domain.Enum.MediaStatus import MediaStatus
import pytest

_fixture = VideoTestFixture()

def test_Instantiate():
    expectedTitle = _fixture.GetValidTitle()
    expectedDescription = _fixture.GetValidDescription()
    expectedYearLaunched = _fixture.GetValidYearLaunched()
    expectedOpened = _fixture.GetRandomBoolean()
    expectedPublished = _fixture.GetRandomBoolean()
    expectedDuration = _fixture.GetValidDuration()
    expectedRating = _fixture.GetRandomRating()

    expectedCreatedDate = datetime.now()
    video = Video(
        expectedTitle, 
        expectedDescription,
        expectedYearLaunched, 
        expectedOpened, 
        expectedPublished,
        expectedDuration,
        expectedRating
    )

    assert video.title == expectedTitle
    assert video.description == expectedDescription
    assert video.YearLaunched == expectedYearLaunched
    assert video.opened == expectedOpened
    assert video.published == expectedPublished
    assert video.duration == expectedDuration
    assert_that(video.createdAt).is_close_to(expectedCreatedDate, timedelta(seconds=10))
    assert video.thumb is None
    assert video.thumbHalf is None
    assert video.banner is None
    assert video.media is None
    assert video.trailer is None

def test_ValidateWhenValidState():
    validVideo = _fixture.GetValidVideo()
    notificationHandler = NotificationValidationHandler()

    validVideo.Validate(notificationHandler)

    assert not notificationHandler.HasErrors()

def test_ValidateWithErrorWhenInvalidState():
    invalidVideo = Video(_fixture.GetTooLongTitle(),
                        _fixture.GetTooLongDescription(),
                        _fixture.GetValidYearLaunched(),
                        _fixture.GetRandomBoolean(),
                        _fixture.GetRandomBoolean(),
                        _fixture.GetValidDuration(),
                        _fixture.GetRandomRating()
                        )

    notificationHandler = NotificationValidationHandler()
    invalidVideo.Validate(notificationHandler)

    assert notificationHandler.HasErrors
    expected_errors = [
        "Title should be less or equal 255 characters long",
        "Description should be less or equal 4000 characters long"
    ]
    assert notificationHandler.Errors == expected_errors
    
    

def test_Update():
    expectedTitle = _fixture.GetValidTitle()
    expectedDescription = _fixture.GetValidDescription()
    expectedYearLaunched = _fixture.GetValidYearLaunched()
    expectedOpened = _fixture.GetRandomBoolean()
    expectedPublished = _fixture.GetRandomBoolean()
    expectedDuration = _fixture.GetValidDuration()
    validVideo = _fixture.GetValidVideo()

    validVideo.Update(
        expectedTitle,
        expectedDescription,
        expectedYearLaunched,
        expectedOpened,
        expectedPublished,
        expectedDuration
    )

    assert validVideo.title == expectedTitle
    assert validVideo.description == expectedDescription
    assert validVideo.YearLaunched == expectedYearLaunched
    assert validVideo.opened == expectedOpened
    assert validVideo.published == expectedPublished
    assert validVideo.duration == expectedDuration

def teste_UpdateWithRating():
    expectedTitle = _fixture.GetValidTitle()
    expectedDescription = _fixture.GetValidDescription()
    expectedYearLaunched = _fixture.GetValidYearLaunched()
    expectedOpened = _fixture.GetRandomBoolean()
    expectedPublished = _fixture.GetRandomBoolean()
    expectedDuration = _fixture.GetValidDuration()
    expectedRating = _fixture.GetRandomRating()
    validVideo = _fixture.GetValidVideo()

    validVideo.Update(
        expectedTitle,
        expectedDescription,
        expectedYearLaunched,
        expectedOpened,
        expectedPublished,
        expectedDuration,
        expectedRating
    )

    assert validVideo.title == expectedTitle
    assert validVideo.description == expectedDescription
    assert validVideo.YearLaunched == expectedYearLaunched
    assert validVideo.opened == expectedOpened
    assert validVideo.published == expectedPublished
    assert validVideo.duration == expectedDuration
    assert validVideo.rating == expectedRating

def test_UpdateWithoutRatingDoesntChangeTheRating():
    video = _fixture.GetValidVideo()
    expectedRating = video.rating

    video.Update(
        _fixture.GetValidTitle(),
        _fixture.GetValidDescription(),
        _fixture.GetValidYearLaunched(),
        _fixture.GetRandomBoolean(),
        _fixture.GetRandomBoolean(),
        _fixture.GetValidDuration()
    )

    assert video.rating == expectedRating

def test_ValidateAfterUpdateToValidState():

    expectedTitle = _fixture.GetValidTitle()
    expectedDescription = _fixture.GetValidDescription()
    expectedYearLaunched = _fixture.GetValidYearLaunched()
    expectedOpened = _fixture.GetRandomBoolean()
    expectedPublished = _fixture.GetRandomBoolean()
    expectedDuration = _fixture.GetValidDuration()
    validVideo = _fixture.GetValidVideo()

    validVideo.Update(
        expectedTitle,
        expectedDescription,
        expectedYearLaunched,
        expectedOpened,
        expectedPublished,
        expectedDuration
    )

    notificationHandler = NotificationValidationHandler()

    validVideo.Validate(notificationHandler)

    assert not notificationHandler.HasErrors()

def test_ValidateGenerateErrorWhenUpdateToInvalidState():

    validVideo = _fixture.GetValidVideo()

    validVideo.Update(   
                _fixture.GetTooLongTitle(),
                _fixture.GetTooLongDescription(),
                _fixture.GetValidYearLaunched(),
                _fixture.GetRandomBoolean(),
                _fixture.GetRandomBoolean(),
                _fixture.GetValidDuration(),
                _fixture.GetRandomRating()                     
    )

    notificationHandler = NotificationValidationHandler()

    validVideo.Validate(notificationHandler)

    assert notificationHandler.HasErrors()
    assert len(notificationHandler.Errors) == 2
    assert notificationHandler.Errors == [
        "Title should be less or equal 255 characters long",
        "Description should be less or equal 4000 characters long"
    ]

def test_UpdateThumb():
    validVideo = _fixture.GetValidVideo()
    validImagePath = _fixture.GetValidImagePath()

    validVideo.UpdateThumb(validImagePath)

    assert validVideo.thumb is not None
    assert validVideo.thumb.path == validImagePath

def test_UpdateThumbHalf():
    validVideo = _fixture.GetValidVideo()
    validImagePath = _fixture.GetValidImagePath()

    validVideo.UpdateThumbHalf(validImagePath)

    assert validVideo.thumbHalf.path is not None
    assert validVideo.thumbHalf.path == validImagePath
    
def test_UpdateBanner():
    validVideo = _fixture.GetValidVideo()
    validImagePath = _fixture.GetValidImagePath()

    validVideo.UpdateBanner(validImagePath)

    assert validVideo.banner.path is not None
    assert validVideo.banner.path == validImagePath

def test_UpdateMedia():
    validVideo = _fixture.GetValidVideo()
    validPath = _fixture.GetValidMediaPath()

    validVideo.UpdateMedia(validPath)

    assert validVideo.media is not None
    assert validVideo.media.FilePath == validPath
    assert len(validVideo._events) == 1
    
def test_UpdateAsSentToEncode():
    validVideo = _fixture.GetValidVideo()
    validPath = _fixture.GetValidImagePath()

    validVideo.UpdateMedia(validPath)

    validVideo.UpdateAsSentToEncode()

    assert validVideo.media.status == MediaStatus.Processing

def test_UpdateAsSentToEncodeWithNoMedia():
    validVideo = _fixture.GetValidVideo()
    
    with pytest.raises(EntityValidationException): 
        validVideo.UpdateAsSentToEncode()

def test_UpdateAsEncodingError():
    validVideo = _fixture.GetValidVideo()
    validPath = _fixture.GetValidMediaPath()
    validVideo.UpdateMedia(validPath)

    validVideo.UpdateAsEncodingError()

    assert validVideo.media.status == MediaStatus.Error
    assert validVideo.media.EncodedPath is None

def test_UpdateAsEncodingErrorThrowsWhenNoMedia():
    validVideo = _fixture.GetValidVideo()
    validPath = _fixture.GetValidMediaPath()

    with pytest.raises(EntityValidationException):
        validVideo.UpdateAsEncodingError()

def test_UpdateAsEncoded():
    validVideo = _fixture.GetValidVideo()
    validPath = _fixture.GetValidMediaPath()
    validEncodedPath = _fixture.GetValidMediaPath()
    validVideo.UpdateMedia(validPath)

    validVideo.UpdateAsEncoded(validEncodedPath)

    assert validVideo.media.status == MediaStatus.Completed
    assert validVideo.media.EncodedPath == validEncodedPath

def test_UpdateAsEncodedThrowsWhenNoMedia():

    validVideo = _fixture.GetValidVideo()
    validPath = _fixture.GetValidMediaPath()
    validEncodedPath = _fixture.GetValidMediaPath()

    with pytest.raises(EntityValidationException):
        validVideo.UpdateAsEncoded(validEncodedPath)

def test_UpdateTrailer():
    validVideo = _fixture.GetValidVideo()
    validPath = _fixture.GetValidMediaPath()

    validVideo.UpdateTrailer(validPath)

    assert validVideo.trailer is not None
    assert validVideo.trailer.FilePath == validPath

def test_AddCategory():
    validVideo = _fixture.GetValidVideo()
    categoryIdExample = uuid.uuid4()

    validVideo.AddCategory(categoryIdExample)

    assert len(validVideo._categories) == 1
    assert validVideo._categories[0] == categoryIdExample

def test_RemoveCategory():
    validVideo = _fixture.GetValidVideo()
    categoryIdExample = uuid.uuid4()
    categoryIdExample2 = uuid.uuid4()

    validVideo.AddCategory(categoryIdExample)
    validVideo.AddCategory(categoryIdExample2)

    validVideo.RemoveCategory(categoryIdExample)

    assert len(validVideo._categories) == 1
    assert validVideo._categories[0] == categoryIdExample2

def test_RemoveAllCategory():
    validVideo = _fixture.GetValidVideo()
    categoryIdExample = uuid.uuid4()
    categoryIdExample2 = uuid.uuid4()

    validVideo.AddCategory(categoryIdExample)
    validVideo.AddCategory(categoryIdExample2)

    validVideo.RemoveAllCategories()

    assert len(validVideo._categories) == 0
    
def test_AddGenre():
    validVideo = _fixture.GetValidVideo()
    genreIdExample = uuid.uuid4()

    validVideo.AddGenre(genreIdExample)

    assert len(validVideo._genres) == 1
    assert validVideo._genres[0] == genreIdExample

def test_RemoveGenre():
    validVideo = _fixture.GetValidVideo()
    genreIdExample = uuid.uuid4()
    genreIdExample2 = uuid.uuid4()

    validVideo.AddGenre(genreIdExample)
    validVideo.AddGenre(genreIdExample2)

    validVideo.RemoveGenre(genreIdExample)

    assert len(validVideo._genres) == 1
    assert validVideo._genres[0] == genreIdExample2

def test_RemoveAllGenre():
    validVideo = _fixture.GetValidVideo()
    genreIdExample = uuid.uuid4()
    genreIdExample2 = uuid.uuid4()

    validVideo.AddGenre(genreIdExample)
    validVideo.AddGenre(genreIdExample2)

    validVideo.RemoveAllGenre()

    assert len(validVideo._genres) == 0

def test_AddCastMember():
    validVideo = _fixture.GetValidVideo()
    castIdExample = uuid.uuid4()

    validVideo.AddCastMember(castIdExample)
    
    assert len(validVideo._castMembers) == 1
    assert validVideo._castMembers[0] == castIdExample

def test_RemoveCastMember():
    validVideo = _fixture.GetValidVideo()
    castIdExample = uuid.uuid4()
    castIdExample2 = uuid.uuid4()

    validVideo.AddCastMember(castIdExample)
    validVideo.AddCastMember(castIdExample2)

    validVideo.RemoveCastMember(castIdExample)

    assert len(validVideo._castMembers) == 1
    assert validVideo._castMembers[0] == castIdExample2

def test_RemoveAllCastMember():
    validVideo = _fixture.GetValidVideo()
    castIdExample = uuid.uuid4()
    castIdExample2 = uuid.uuid4()

    validVideo.AddCastMember(castIdExample)
    validVideo.AddCastMember(castIdExample2)

    validVideo.RemoveAllCastMembers()

    assert len(validVideo._castMembers) == 0



    