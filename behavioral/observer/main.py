from abc import ABC, abstractmethod
from enum import Enum


class EventType(Enum):
    OPEN = "open"
    SAVE = "save"


class Subscriber(ABC):
    @abstractmethod
    def get_info(self) -> str:
        pass

    @abstractmethod
    def update(file_name: str) -> None:
        pass


class EventManager:
    def __init__(self):
        self._subscribers: dict[Subscriber, set[EventType]] = {}

    def subscribe(self, subscriber: Subscriber, eventType: EventType) -> None:
        subscriberEvents = self._subscribers.get(subscriber, set())
        subscriberEvents.add(eventType)
        self._subscribers[subscriber] = subscriberEvents

    def unsubscribe(self, subscriber: Subscriber, eventType: EventType) -> None:
        subscriberEvents = self._subscribers.get(subscriber, set())
        subscriberEvents.remove(eventType)
        self._subscribers[subscriber] = subscriberEvents
    
    def notify(self, file_name: str, eventType: EventType) -> None:
        for subscriber, eventTypes in self._subscribers.items():
            if eventType in eventTypes:
                subscriber.update(file_name)

    def display_subscriptions(self) -> None:
        for subscriber, eventTypes in self._subscribers.items():
            print(f"INFO: {subscriber.get_info()}, events: {eventTypes}")


class DBSubscriber(Subscriber):
    def get_info(self) -> str:
        return "I'm Postgres Database subscriber!"

    def update(self, file_name: str) -> None:
        print("updating staff on Postgres DB side...")


class EmailSubscriber(Subscriber):
    def get_info(self) -> str:
        return "I'm AWS SNS subscriber!"

    def update(self, file_name: str) -> None:
        print("some file was just opened, doing my stuff...")


def main() -> None:
    manager = EventManager()
    dbSubscriber = DBSubscriber()
    emailSubscriber = EmailSubscriber()

    manager.subscribe(dbSubscriber, EventType.SAVE)
    manager.subscribe(emailSubscriber, EventType.OPEN)
    manager.notify("test.txt", EventType.OPEN)
    manager.notify("test.txt", EventType.SAVE)

    manager.display_subscriptions()

if __name__ == "__main__":
    main()
