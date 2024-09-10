import os

from .factories import LinuxButtonFactory, WindowsButton


OS_NAME = os.environ['OS_NAME']

match OS_NAME:
    case 'Linux':
        button = LinuxButtonFactory()
    case 'Windows':
        button = WindowsButton()
    case _:
        raise NotImplementedError('No such button!')

button.common_logic()
