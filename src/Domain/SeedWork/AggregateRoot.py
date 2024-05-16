from typing import List
from src.Domain.SeedWork.DomainEvent import DomainEvent
from src.Domain.SeedWork.Entity import Entity

class AggregateRoot(Entity):
    def __init__(self):
        super().__init__()
        self._events:List[DomainEvent] = []
    
    def RaiseEvent(self, event:DomainEvent):
        self._events.append(event)
    
    def ClearEvents(self):
        self._events.clear()
