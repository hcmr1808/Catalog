from typing import Optional
from src.Domain.Enum.MediaStatus import MediaStatus
from src.Domain.SeedWork.Entity import Entity

class Media(Entity):

    def __init__(self, FilePath:str):
        super().__init__()
        self.FilePath = FilePath
        self.status = MediaStatus.Pending
        self.EncodedPath = None
    
    def UpdateAsSentToEncode(self):
        self.status = MediaStatus.Processing

    def UpdateAsEncoded(self, encodedExamplePath:str):
        self.status = MediaStatus.Completed
        self.EncodedPath = encodedExamplePath
    
    def UpdateAsEncodingError(self):
        self.status = MediaStatus.Error
        self.EncodedPath = None
