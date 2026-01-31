from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    x: float
    y: float


class VehicleStrategy(ABC):
    @abstractmethod
    def get_route(self) -> list[Location]:
        ...


class WalkingStrategy(VehicleStrategy):
    def get_route(self) -> list[Location]:
        return [
            Location(0, 1),
            Location(1, 10),
        ]


class BikeStrategy(VehicleStrategy):
    def get_route(self) -> list[Location]:
        return [
            Location(1, 3),
            Location(10, 11),
        ]


class TravelPlanner:
    def __init__(self) -> None:
        self._strategy: VehicleStrategy | None = None
    
    def setStrategy(self, strategy: VehicleStrategy) -> None:
        self._strategy = strategy

    def get_journey(self) -> None:
        for idx, location in enumerate(self._strategy.get_route(), start=1):
            print(f"{idx}: x: {location.x}, y: {location.y}")


def main() -> None:
    planner = TravelPlanner()
    planner.setStrategy(BikeStrategy())
    planner.get_journey()


if __name__ == "__main__":
    main()
