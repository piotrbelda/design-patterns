from abc import ABC, abstractmethod
from math import sqrt


class RoundPeg(ABC):
    @abstractmethod
    def get_radius(self) -> int:
        pass


class RoundHole:
    def __init__(self, radius: int) -> None:
        self.radius = radius
    
    def fits(self, peg: RoundPeg) -> None:
        print("fits" if self.radius >= peg.get_radius() else "doesn't fit :(")


class SquarePeg:
    def __init__(self, width: int) -> None:
        self.width = width


class SquarePegAdapter(RoundPeg):
    def __init__(self, squarePeg: SquarePeg) -> None:
        self.squarePeg = squarePeg

    def get_radius(self) -> int:
        return self.squarePeg.width * sqrt(2) / 2


hole = RoundHole(5)
squarePeg = SquarePeg(7)
squarePegAdapter = SquarePegAdapter(squarePeg)

hole.fits(squarePegAdapter)
