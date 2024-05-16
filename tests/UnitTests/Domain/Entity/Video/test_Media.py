from tests.UnitTests.Domain.Entity.Video.VideoTestFixture import VideoTestFixture
from src.Domain.Entity.Media import Media
from src.Domain.Enum.MediaStatus import MediaStatus
import pytest

_fixture = VideoTestFixture()

def test_Instantiate():
    expectedFilePath = _fixture.GetValidMediaPath()

    media = Media(expectedFilePath)

    assert media.id != ""
    assert media.FilePath == expectedFilePath
    assert media.status == MediaStatus.Pending

def test_UpdateAsSentToEncode():
    media = _fixture.GetValidMedia()
    media.UpdateAsSentToEncode()
    assert media.status == MediaStatus.Processing

def test_UpdateAsEncoded():
    media = _fixture.GetValidMedia()
    encodedPath = _fixture.GetValidMediaPath()
    media.UpdateAsSentToEncode()

    media.UpdateAsEncoded(encodedPath)
    assert media.status == MediaStatus.Completed
    assert media.EncodedPath == encodedPath

def test_UpdateAsEncodingError():
    media = _fixture.GetValidMedia()
    media.UpdateAsSentToEncode()

    media.UpdateAsEncodingError()
    assert media.status == MediaStatus.Error
    assert media.EncodedPath is None