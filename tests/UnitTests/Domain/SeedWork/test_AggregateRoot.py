from tests.UnitTests.Domain.SeedWork.AggregateRootFake import AggregateRootFake
from tests.UnitTests.Domain.SeedWork.DomainEventFake import DomainEventFake

def test_RaiseEvent():
    domainEvent = DomainEventFake()
    aggregate = AggregateRootFake()

    aggregate.RaiseEvent(domainEvent)

    assert len(aggregate._events) == 1

def test_ClearEvents():
    domainEvent = DomainEventFake()
    aggregate = AggregateRootFake()

    aggregate.RaiseEvent(domainEvent)
    aggregate.ClearEvents()

    assert len(aggregate._events) == 0