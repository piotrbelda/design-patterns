from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


class GraphicBox(Graphic):
    def __init__(self) -> None:
        self._objects: List[Graphic] = []

    def move(self, x: int, y: int) -> None:
        for object in self._objects:
            object.move(x, y)
    
    def draw(self) -> None:
        for object in self._objects:
            object.draw()

    def add_object(self, object: Graphic) -> None:
        self._objects.append(object)

    def remove_object(self, index: int) -> None:
        self._objects.pop(index)


class Dot(Graphic):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(self.__str__())


class Circle(Dot):
    def __init__(self, x: int, y: int, r: int) -> None:
        super().__init__(x, y)
        self.r = r



if __name__ == "__main__":
    main_component = GraphicBox()
    sub_component = GraphicBox()
    dot_2 = Dot(2, 3)
    circle_2 = Circle(1, 2, 3)
    sub_component.add_object(dot_2)
    sub_component.add_object(circle_2)
    dot_1 = Dot(1, 2)
    main_component.add_object(dot_1)
    main_component.add_object(sub_component)

    # this command draws all the sub elements!
    main_component.draw()
