"""GPIO rotary encoder adapter for a Raspberry Pi Pico."""

from machine import Pin


class I2CRelEncoder:
    def __init__(self, pins=(14, 15, 13)):
        self.pin_a = Pin(pins[0], Pin.IN, Pin.PULL_UP)
        self.pin_b = Pin(pins[1], Pin.IN, Pin.PULL_UP)
        self.pin_button = Pin(pins[2], Pin.IN, Pin.PULL_UP)
        self._last = (self.pin_a.value() << 1) | self.pin_b.value()
        self._position = 0

    @property
    def rel_position(self):
        self._poll()
        return self._position

    @property
    def button(self):
        return not self.pin_button.value()

    def reset(self):
        self._position = 0

    def _poll(self):
        current = (self.pin_a.value() << 1) | self.pin_b.value()
        transitions = ((self._last << 2) | current) & 0x0F
        self._last = current
        if transitions in (1, 7, 8, 14):
            self._position += 1
        elif transitions in (2, 4, 11, 13):
            self._position -= 1
