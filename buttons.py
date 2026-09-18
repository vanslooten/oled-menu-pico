import machine
import utime

"""
Push button test script.

To wire a push button to a Raspberry Pi Pico using the internal pull-up resistor,
connect one side of the button to a chosen GPIO pin (like GP13) and the other side to a GND (ground) pin.
No external resistors or extra wires are needed.

Wiring Steps
GPIO Pin: Connect one pin of the button to GP13 (pin 19) on the Pico.
Ground Pin: Connect the opposite pin of the button to any GND pin.

How It Works
Not Pressed: The internal pull-up resistor holds the pin at HIGH (3.3V).
Pressed: The button connects the pin directly to GND, changing the reading to LOW (0V).
"""

# Set up GP13..15 as an input for the buttons with an internal pull-up resistor
button1 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button3 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if button1.value() == 0:  # Button pressed reads LOW
        print("Button 1 pressed!")
    if button2.value() == 0:
        print("Button 2 pressed!")
    if button3.value() == 0:
        print("Button 3 pressed!")
    utime.sleep(0.2)
