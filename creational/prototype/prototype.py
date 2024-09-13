import copy


class SelfReferencingEntity:
    def __init__(self) -> None:
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Component:
    def __init__(self, number, iterable, circular_ref) -> None:
        self.number = number
        self.iterable = iterable
        self.circular_ref = circular_ref
    
    def __copy__(self):
        iterable = copy.copy(self.iterable)
        circular_ref = copy.copy(self.circular_ref)

        new = self.__class__(self.number, iterable, circular_ref)
        new.__dict__.update(self.__dict__)
        
        return new

    def __deepcopy__(self, memo=None):
        memo = memo or {}
        iterable = copy.deepcopy(self.iterable, memo)
        circular_ref = copy.deepcopy(self.circular_ref, memo)

        new = self.__class__(self.number, iterable, circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == '__main__':
    list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
    circular_ref = SelfReferencingEntity()
    component = Component(23, list_of_objects, circular_ref)
    circular_ref.set_parent(component)

    shallow_copied_component = copy.copy(component)
    shallow_copied_component.iterable[-1] = "new object"

    deep_copied_component = copy.deepcopy(component)
    deep_copied_component.iterable[-1] = 'another object'
    deep_copied_component.iterable[1].add(4)
