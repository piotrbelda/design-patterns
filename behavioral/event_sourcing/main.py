from event_store import EventStore
from inventory import Inventory
from item import Item


def main() -> None:
    store = EventStore()
    inventory = Inventory(store)

    item1 = Item("sword", "rare", "castle")
    item2 = Item("sword", "rare", "battleground")
    item3 = Item("sword", "rare", "shop")
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)

    print(inventory.get_items())
    print(inventory.get_count("sword"))


if __name__ == "__main__":
    main()
