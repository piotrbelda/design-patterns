from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def on_click(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass


class LinuxButton(Button):
    @abstractmethod
    def on_click(self):
        pass


class MacButton(Button):
    @abstractmethod
    def on_click(self):
        pass


class LinuxCheckbox(ABC):
    @abstractmethod
    def render(self):
        pass


class MacCheckbox(ABC):
    @abstractmethod
    def render(self):
        pass
