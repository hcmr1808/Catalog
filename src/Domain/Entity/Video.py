from src.Domain.Entity.Media import Media
from src.Domain.Exceptions.EntityValidationException import EntityValidationException
from src.Domain.SeedWork.AggregateRoot import AggregateRoot
from src.Domain.Enum.Rating import Rating
from src.Domain.Validation.ValidationHandler import ValidationHandler
from src.Domain.Validator.VideoValidator import VideoValidator
from src.Domain.ValueObjects.Image import Image
from src.Domain.Events.VideoUploadedEvent import VideoUploadedEvent
from typing import Optional, List
import datetime
import uuid

class Video(AggregateRoot):
    def __init__(self,
                title, 
                description, 
                YearLaunched:int, 
                opened:bool, 
                published:bool, 
                duration:int, 
                rating:Rating,
                thumb:Optional[Image] = None,
                thumbHalf:Optional[Image] = None,
                banner:Optional[Image] = None,
                media:Optional[Media] = None,
                trailer:Optional[Media] = None
                ):
        super().__init__()
        self.title = title
        self.description = description
        self.YearLaunched = YearLaunched 
        self.opened = opened
        self.published = published
        self.duration = duration
        self.rating = rating
        self.thumb:Optional[Image] = None
        self.thumbHalf:Optional[Image] = None
        self.banner:Optional[Image] = None
        self.media:Optional[Media] = None
        self.trailer:Optional[Media] = None

        self._categories = []
        self._genres = []
        self._castMembers = []

        self.createdAt = datetime.datetime.now()

    def Validate(self, handler:ValidationHandler):
        VideoValidator(self, handler).Validate()
    
    def Update(self, 
               title, 
               description, 
               YearLaunched:int, 
               opened:bool, 
               published:bool, 
               duration:int, 
               rating:Optional[Rating] = None
            ):
        self.title = title
        self.description = description
        self.YearLaunched = YearLaunched
        self.opened = opened
        self.published = published
        self.duration = duration
        if rating is not None:
            self.rating = Rating(rating)

    def UpdateThumb(self, path):
        self.thumb = Image(path)
        

    def UpdateThumbHalf(self, path:str):
        self.thumbHalf = Image(path)

    def UpdateBanner(self, path:str):
        self.banner = Image(path)

    def UpdateMedia(self, path:str):
        self.media = Media(path)
        event = VideoUploadedEvent(self.media.id, path)
        self.RaiseEvent(event)
    
    def UpdateTrailer(self, path:str):
        self.trailer = Media(path)
    
    def UpdateAsSentToEncode(self):
        if self.media is None:
            raise EntityValidationException("There is no Media")
        self.media.UpdateAsSentToEncode()
    
    def UpdateAsEncoded(self, validEncodedPath):
        if self.media is None:
            raise EntityValidationException("There is no Media")
        self.media.UpdateAsEncoded(validEncodedPath)
    
    def UpdateAsEncodingError(self):
        if self.media is None:
            raise EntityValidationException("There is no Media")
        self.media.UpdateAsEncodingError()
    
    def AddCategory(self, categoryId:uuid.UUID):
        self._categories.append(categoryId)
    
    def RemoveCategory(self, categoryId:uuid.UUID):
        self._categories.remove(categoryId)

    def RemoveAllCategories(self):
        self._categories = []
    
    def AddGenre(self, genreId:uuid.UUID):
        self._genres.append(genreId)

    def RemoveGenre(self, genreId:uuid.UUID):
        self._genres.remove(genreId)

    def RemoveAllGenre(self):
        self._genres = [] 
    
    def AddCastMember(self, castId:uuid.UUID):
        self._castMembers.append(castId)
    
    def RemoveCastMember(self, castId:uuid.UUID):
        self._castMembers.remove(castId)
    
    def RemoveAllCastMembers(self):
        self._castMembers = []



    



        
        

    
