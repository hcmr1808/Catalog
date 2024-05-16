from enum import Enum

class MediaStatus(Enum):
    Pending = 0
    Processing = 1
    Completed = 2
    Error = 3