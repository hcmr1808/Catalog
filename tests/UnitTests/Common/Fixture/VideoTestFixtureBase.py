from src.Common.FileInput import FileInput
from random import randint
from src.Domain.Entity.Media import Media
from src.Domain.Entity.Video import Video
from src.Domain.Enum.Rating import Rating
import random
from tests.UnitTests.Common.BaseFixture import BaseFixture
from faker import Faker
import datetime
from io import BytesIO

class VideoTestFixtureBase(BaseFixture):

    def __init__(self):
        super().__init__()
    
    def GetValidVideo(self) -> Video:
        return Video( 
            self.GetValidTitle(),
            self.GetValidDescription(),
            self.GetValidYearLaunched,
            self.GetRandomBoolean(),
            self.GetRandomBoolean(),
            self.GetValidDuration(),
            self.GetRandomRating())

    def GetValidVideoWithAllProperties(self):
        video = Video(
            self.GetValidTitle(),
            self.GetValidDescription(),
            self.GetValidYearLaunched,
            self.GetRandomBoolean(),
            self.GetRandomBoolean(),
            self.GetValidDuration(),
            self.GetRandomRating()
        )
        video.UpdateThumb(self.GetValidImagePath())
        video.UpdateThumHalf(self.GetValidImagePath())
        video.UpdateBanner(self.GetValidImagePath())

        
    
    def GetRandomRating(self):
        enumValue = list(Rating)
        return random.choice(enumValue)

    def GetValidTitle(self):
        title = self.faker.name()
        return title

    def GetValidDescription(self):
        description = self.faker.sentence()
        return description

    def GetTooLongDescription(self):
        data = ['a' for _ in range(4100)]
        description = ''.join(data)
        return description

    def GetValidYearLaunched(self):
        start_date = datetime.datetime.strptime("1960-01-01", "%Y-%m-%d")
        end_date = datetime.datetime.strptime("2022-01-01", "%Y-%m-%d")
        random_date = self.faker.date_between(start_date=start_date, end_date=end_date)
        
        return random_date.year
    
    def GetValidDuration(self):
        duration = randint(100, 300)
        return duration
    
    def GetTooLongTitle(self):
        data = ['a' for _ in range(410)]
        title = ''.join(data)
        return title

    def GetValidImagePath(self):
        image_url = self.faker.image_url(width=640, height=480)
        return image_url
    
    def GetValidMediaPath(self):
        exampleMedias = [
            "https://www.googlestorage.com/file-example.mp4",
            "https://www.storage.com/another-example-of-video.mp4",
            "https://www.S3.com.br/example.mp4",
            "https://www.glg.io/file.mp4"
        ]
        return random.choice(exampleMedias)
        
    def GetValidImageFileInput(self):
        example_stream = BytesIO(b"test")
        file_input = FileInput("jpg", example_stream, "image/jpeg")
        return file_input
    
    def GetValidMediaFileInput():
        exampleStream = BytesIO(b"test")
        fileInput = FileInput("mp4", exampleStream, "video/mp4")
        return fileInput
    
    def GetValidMedia(self):
        valid_media_path = self.GetValidMediaPath()
        return Media(valid_media_path)

video = VideoTestFixtureBase()
data = video.GetValidImagePath()
print(data)
#content = data.file_content.read()
#print(content)