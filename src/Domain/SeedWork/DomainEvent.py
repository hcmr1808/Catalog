from abc import ABC
import datetime

class DomainEvent(ABC):
    
    def __init__(self):
        self.ocurredOn = datetime.datetime.now()

    