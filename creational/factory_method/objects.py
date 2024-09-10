from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def on_click(self):
        pass

    @abstractmethod
    def render(self):
        pass


class LinuxButton(Button):
    def on_click(self):
        # action specific for Linux
        pass

    def render(self):
        # Linux-styled button
        pass


class WindowsButton(Button):
    def on_click(self):
        # action specific for Windows
        pass

    def render(self):
        # Windows-styled button
        pass
