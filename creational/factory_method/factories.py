from abc import ABC, abstractmethod

from .objects import Button, LinuxButton, WindowsButton


class ButtonFactory(ABC):
    @abstractmethod
    def factory_method(self) -> Button:
        pass

    def common_logic(self):
        button = self.factory_method()
        button.on_click()
        button.render()


class LinuxButtonFactory(ButtonFactory):
    def factory_method(self) -> LinuxButton:
        # some additional code for creating Linux button
        return LinuxButton()


class LinuxButtonFactory(ButtonFactory):
    def factory_method(self) -> WindowsButton:
        # some additional code for creating Windows button
        return WindowsButton()
