# Raspberry Pi Pico OLED Menu

## Quick setup

1. Install MicroPython on your Raspberry Pi Pico or Pico W.
2. Open this project in VS Code with the MicroPico extension.
3. Connect a 128x64 SSD1306 I2C OLED and three push buttons as shown below.
4. Upload the project files to the Pico.
5. Run one of the test scripts from MicroPico.

The script uses the Pico's internal pull-up resistors. Connect the other side of every button to GND. A button is active when its GPIO pin is connected to GND.

## Wiring

### OLED

The examples use I2C bus 1:

| OLED | Pico |
| --- | --- |
| VCC | 3.3V |
| GND | GND |
| SDA | GP10 |
| SCL | GP11 |

The menu automatically detects OLED address `0x3C` or `0x3D`.

### Buttons

| Function | Pico GPIO |
| --- | --- |
| SELECT | GP13 |
| DOWN | GP14 |
| UP | GP15 |

## Controls

- **UP** moves to the previous menu item.
- **DOWN** moves to the next menu item.
- **SELECT** opens or selects the focused item.
- In a range item, **UP** increases the value and **DOWN** decreases it.
- Press **SELECT** again to confirm a range or combo selection.

## Examples

- `test_combo.py` demonstrates labels and a combo selection.
- `test_screen.py` demonstrates a range value and a custom dashboard screen.
- `test.py` demonstrates disabled items, range values, and enabling an item after selection.
- `blink.py` is a standalone Pico LED blink test.
- `buttons.py` is a standalone button input test.

## Project structure

```text
.
├── buttons.py          # Standalone button test
├── blink.py            # Standalone LED test
├── test.py             # Range and enabled-item example
├── test_combo.py       # Combo menu example
├── test_screen.py      # Custom screen example
└── lib/
    ├── oledmenu.py    # Menu, range, combo, screen, and button controller
    ├── ssd1306.py     # SSD1306 I2C display driver
    └── i2cenc.py      # Legacy GPIO rotary encoder adapter
```

## Using the menu in your own script

Place your script in the project root and import the menu library:

```python
from machine import I2C, Pin
from oledmenu import OLED_MENU

i2c = I2C(1, sda=Pin(10), scl=Pin(11), freq=400000)
menu = OLED_MENU(i2c)
menu.add_label("start", "Start")
menu.start()

while True:
    if menu.update():
        entry = menu.selected
        if entry:
            print("%s selected" % entry)
```

The default `ButtonController` uses SELECT=GP13, DOWN=GP14, and UP=GP15. Custom pins can be supplied with `button_pins=(select, down, up)` when constructing `OLED_MENU`.

## Requirements

- Raspberry Pi Pico or Pico W
- MicroPython firmware
- VS Code with MicroPico
- 128x64 SSD1306 I2C OLED
- Three momentary push buttons
