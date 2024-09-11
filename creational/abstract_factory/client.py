from .factories import LinuxFactory, MacFactory


class Application:
    def __init__(self, os_name) -> None:
        match os_name:
            case 'Linux':
                self.factory = LinuxFactory()
            case 'Mac':
                self.factory = MacFactory()
            case _:
                raise NotImplementedError('No such operation system!')

    def some_logic(self):
        button = self.factory.create_button()
        button.on_click()

        checkbox = self.factory.create_checkbox()
        checkbox.render()
