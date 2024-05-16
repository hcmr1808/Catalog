from src.Domain.SeedWork.DomainEvent import DomainEvent

class DomainEventFake(DomainEvent):
    def __init__(self):
        super().__init__()