from src.Domain.SeedWork.DomainEvent import DomainEvent
import uuid

class VideoUploadedEvent(DomainEvent):

    def __init__(self, resourceId:uuid.UUID, filePath:str):
        super().__init__()
        self.resourceId = resourceId
        self.filePath = filePath
    
    