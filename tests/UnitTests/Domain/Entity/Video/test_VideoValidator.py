from src.Domain.Entity.Video import Video
from src.Domain.Validation.NotificationValidationHandler import NotificationValidationHandler
from src.Domain.Validator.VideoValidator import VideoValidator
from tests.UnitTests.Domain.Entity.Video.VideoTestFixture import VideoTestFixture


_fixture = VideoTestFixture()

def test_ReturnsValidWhenVideoIsValid():
    validVideo = _fixture.GetValidVideo()
    notificationValidationHandler = NotificationValidationHandler()

    videoValidator = VideoValidator(validVideo, notificationValidationHandler)

    videoValidator.Validate()

    assert notificationValidationHandler.HasErrors() is False
    assert len(notificationValidationHandler.Errors) == 0

def test_ReturnsErrorWhenTitleIsTooLong():
    invalidVideo = Video(
        _fixture.GetTooLongTitle(),
        _fixture.GetValidDescription(),
        _fixture.GetValidYearLaunched(),
        _fixture.GetRandomBoolean(),
        _fixture.GetRandomBoolean(),
        _fixture.GetValidDuration(),
        _fixture.GetRandomRating()
    )

    notificationValidationHandler = NotificationValidationHandler()
    videoValidator = VideoValidator(invalidVideo, notificationValidationHandler)

    videoValidator.Validate()

    assert notificationValidationHandler.HasErrors() is True
    assert len(notificationValidationHandler.Errors) == 1

def test_ReturnsErrorWhenTitleIsEmpty():
    invalidVideo = Video(
        "",
        _fixture.GetValidDescription(),
        _fixture.GetValidYearLaunched(),
        _fixture.GetRandomBoolean(),
        _fixture.GetRandomBoolean(),
        _fixture.GetValidDuration(),
        _fixture.GetRandomRating()
    )

    notificationValidationHandler = NotificationValidationHandler()
    videoValidator = VideoValidator(invalidVideo, notificationValidationHandler)

    videoValidator.Validate()

    assert notificationValidationHandler.HasErrors() is True
    assert len(notificationValidationHandler.Errors) == 1

def test_ReturnsErrorWhenDescriptionIsTooLong():
    invalidVideo = Video(
        _fixture.GetValidTitle(),
        _fixture.GetTooLongDescription(),
        _fixture.GetValidYearLaunched(),
        _fixture.GetRandomBoolean(),
        _fixture.GetRandomBoolean(),
        _fixture.GetValidDuration(),
        _fixture.GetRandomRating()
    )

    notificationValidationHandler = NotificationValidationHandler()
    videoValidator = VideoValidator(invalidVideo, notificationValidationHandler)

    videoValidator.Validate()

    assert notificationValidationHandler.HasErrors() is True
    assert len(notificationValidationHandler.Errors) == 1

def test_ReturnsErrorWhenDescriptionIsEmpty():
    invalidVideo = Video(
        _fixture.GetValidTitle(),
        "",
        _fixture.GetValidYearLaunched(),
        _fixture.GetRandomBoolean(),
        _fixture.GetRandomBoolean(),
        _fixture.GetValidDuration(),
        _fixture.GetRandomRating()
    )

    notificationValidationHandler = NotificationValidationHandler()
    videoValidator = VideoValidator(invalidVideo, notificationValidationHandler)

    videoValidator.Validate()

    assert notificationValidationHandler.HasErrors() is True
    assert len(notificationValidationHandler.Errors) == 1