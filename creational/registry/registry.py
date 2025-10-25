from typing import Any, Callable

type Data = dict[str, Any]
type DataFunc = Callable[[Data], None]

_func_registry: dict[str, DataFunc] = {}


def register_func(data_type: str):
    def register_wrapped_func(func: DataFunc):
        def wrapper(*args, **kwargs):
            print("I was decorated with registerFunc!!!")
            return func(*args, **kwargs)

        _func_registry[data_type] = wrapper
        return wrapper

    return register_wrapped_func


@register_func("json")
def process_data_json(data: Data) -> None:
    print("processing data in JSON format")


@register_func("xml")
def process_data_xml(data: Data) -> None:
    print("processing data in XML format")


@register_func("csv")
def process_data_csv(data: Data) -> None:
    print("processing data in CSV format")


def run_function(format: str):
    if not (fn := _func_registry.get(format)):
        raise KeyError(f"Format: {format} not registered!")
    
    fn({"test": 123})


if __name__ == "__main__":
    run_function("csv")
