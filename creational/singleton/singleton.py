from typing import Any


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, x: int, y: str) -> None:
        self.x = x
        self.y = y

    def some_logic(self):
        pass


if __name__ == '__main__':
    s1 = Singleton(1, '2')
    s2 = Singleton(2, '3')

    assert s1 is s2
    assert s1.x == s2.x
    assert s1.y == s2.y
