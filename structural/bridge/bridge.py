from abc import ABC, abstractmethod


class Remote:
    def __init__(self, device: "Device") -> None:
        self._device = device

    def oneChannelUp(self):
        currentChannel = self._device.get_channel()
        self._device.set_channel(currentChannel + 1)

    def oneChannelDown(self):
        currentChannel = self._device.get_channel()
        self._device.set_channel(currentChannel - 1)

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.turn_off()
        else:
            self._device.turn_on()


class Device(ABC):
    def __init__(self) -> None:
        self._is_running = False
        self._current_channel = 0

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def is_enabled(self):
        return self._is_running


class TV(Device):
    def get_channel(self):
        # return TV channel number
        pass

    def set_channel(self, channel):
        # set channel
        pass

    def turn_on(self):
        # turn on TV
        pass

    def turn_off(self):
        # turn off TV
        pass


class Radio(Device):
    def get_channel(self):
        # return Radion channel number
        pass

    def set_channel(self, channel):
        # set channel
        pass

    def turn_on(self):
        # turn on Radion
        pass

    def turn_off(self):
        # turn off Radio
        pass


if __name__ == "__main__":
    device = TV()
    remote = Remote(device)
    remote.toggle_power()
    remote.oneChannelDown()
    remote.oneChannelUp()
    remote.toggle_power()
