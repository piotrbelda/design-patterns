from collections import Counter
from functools import cache

from event import Event, EventType
from event_store import EventStore
from item import Item


class Inventory:
    def __init__(self, store: EventStore[Item]) -> None:
        self.store = store

    def add_item(self, item: Item) -> None:
        event = Event(EventType.ITEM_ADDED, item)
        self.store.append(event)
        self._invalidate_cache()

    def remove_item(self, item: Item) -> None:
        if self.get_count(item) <= 0:
            raise ValueError(f"{item} not in inventory.")

        event = Event(EventType.ITEM_REMOVED, item)
        self.store.append(event)
        self._invalidate_cache()

    def _invalidate_cache(self) -> None:
        self.get_items.cache_clear()

    @cache
    def get_items(self) -> list[tuple[str, int]]:
        counts = Counter[str]()
        for event in self.store.get_all_events():
            name = event.data.name
            if event.type == EventType.ITEM_ADDED:
                counts[name] += 1
            elif event.type == EventType.ITEM_REMOVED:
                counts[name] -= 1

        return [
            (item, count) for item, count in counts.items() if count > 0
        ]

    def get_count(self, name: str) -> int:
        return dict(self.get_items()).get(name, 0)
