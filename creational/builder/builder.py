from abc import ABC, abstractmethod

from .results import House, Project


class Engineer(ABC):
    @abstractmethod
    def make_foundations(self):
        pass

    @abstractmethod
    def raise_wall(self, side: str):
        pass

    @abstractmethod
    def create_roof(self):
        pass

    @abstractmethod
    def mount_insulation(self):
        pass

    @abstractmethod
    def paint(self):
        pass

    @abstractmethod
    def install_waterpool(self):
        pass

    @abstractmethod
    def make_garage(self):
        pass

    @abstractmethod
    def get_results(self):
        pass


class FieldEngineer(ABC):
    @abstractmethod
    def make_foundations(self):
        # create foundations
        pass

    @abstractmethod
    def raise_wall(self, side: str):
        # raise wall
        pass

    @abstractmethod
    def create_roof(self):
        # setup roof
        pass

    @abstractmethod
    def mount_insulation(self):
        # make insulation on each wall
        pass

    @abstractmethod
    def paint(self):
        # paint building
        pass

    @abstractmethod
    def install_waterpool(self):
        # dig a hole and fill it with water
        pass

    @abstractmethod
    def make_garage(self):
        # setup garage
        pass

    def get_results(self) -> House:
        pass


class Drafter(ABC):
    @abstractmethod
    def make_foundations(self):
        # draw foundations
        pass

    @abstractmethod
    def raise_wall(self, side: str):
        # draw wall
        pass

    @abstractmethod
    def create_roof(self):
        # draw roof
        pass

    @abstractmethod
    def mount_insulation(self):
        # draw insulation
        pass

    @abstractmethod
    def paint(self):
        # paint
        pass

    @abstractmethod
    def install_waterpool(self):
        # draw waterpool
        pass

    @abstractmethod
    def make_garage(self):
        # draw garage
        pass

    def get_results(self) -> Project:
        pass
