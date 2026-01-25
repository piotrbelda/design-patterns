from functools import wraps
from typing import Callable

type PredicateFn[T] = Callable[[T], bool]


class Predicate[T]:
    def __init__(self, function: PredicateFn[T]):
        self.function = function

    def __call__(self, obj: T) -> bool:
        return self.function(obj)

    def __and__(self, predicate: "Predicate[T]") -> "Predicate[T]":
        return Predicate(lambda user: self(user) and predicate(user))

    def __or__(self, predicate: "Predicate[T]") -> "Predicate[T]":
        return Predicate(lambda user: self(user) or predicate(user))

    def __invert__(self) -> "Predicate[T]":
        return Predicate(lambda user: not self(user))


def predicate[T](function: PredicateFn[T]) -> Predicate[T]:
    @wraps(function)
    def wrapper(obj: T) -> bool:
        return function(obj)

    return Predicate(wrapper)
