# MicroPython for Internet of Things - Kiwi PyCon XIII / Kiwi PyCon XIV

Kiwi PyCon XIII workshop that explores the use of MicroPython on a Raspberry Pi Pico board in an Internet of Things context. Dr Glenn Ramsey conducted the workshop.

Kiwi PyCon XIV workshop explored the use of MicroPython on a ESP32 board. Dr Glenn Ramsey & William Hamilton conducted the workshop.

## Hardware Kiwi PyCon XIII
* [RasberryPi Pico WH](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#raspberry-pi-pico-w-and-pico-wh)
* [KY-038 Sound Detection Module](https://www.datasheethub.com/ky-038-lm393-sound-detection-module/)

## Hardware Kiwi PyCon XIV
* [ESP32-C3](https://www.espressif.com/en/products/socs/esp32-c3)
* [KY-037 Sound Detection Module](https://arduinomodules.info/ky-037-high-sensitivity-sound-detection-module/)

## Documentation
* [MicroPython documentation](https://docs.micropython.org/)

## Getting Started
* Create a new Python venv

```
python3 -m venv venv
. venv/bin/activate
```

*  Install `mpremote`.
```
pip install mpremote
```

### RasberryPi Pico WH
*  Download and copy [MicroPython for Raspberry Pi Pico W with Wi-Fi and Bluetooth LE support](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).

```
cp RPI_PICO_W-20240602-v1.23.0.uf2 /Volumes/RPI-RP2/
```

### ESP32-C3
* Install [`esptool`](https://docs.espressif.com/projects/esptool/en/latest/esp32/).
* Download [firmware](https://micropython.org/download/ESP32_GENERIC_C3/).
* Erase entire flash.
    ```
    esptool erase_flash
    ```
* Flash MicroPython firmware.
    ```
    esptool --baud 460800 write_flash 0 <firmware>
    ```

## Test `mpremote` access.
```
mpremote help
mpremote devs # list connected devices
mpremote repl # Python shell. Press `Ctrl` + `b`.
```

## Blink - RasberryPi Pico WH

```
mpremote fs cp blink.py :blink.py
mpremote repl
```

```
MicroPython v1.23.0 on 2024-06-02; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> import blink
```

## WiFi - RasberryPi Pico WH

* Update `SSID` and `PASSWORD` to match your WiFi connection.
* Update `connection.ifconfig()`:
```
connection.ifconfig(
  [
    "IP address",
    "subnet mask",
    "gateway",
    "DNS"
  ]
)
```

* Copy `wifi.py` and run.

```
mpremote fs cp wifi.py :wifi.py
mpremote repl
```

```
MicroPython v1.23.0 on 2024-06-02; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> import wifi
>>> wifi.main()
```

## Temperature - RasberryPi Pico WH

```
mpremote fs cp temp.py :temp.py
mpremote repl
```

```
MicroPython v1.23.0 on 2024-06-02; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> import temp
```

## Button - ESP32-C3

```
mpremote fs cp button.py :button.py
mpremote repl
```

```
Connected to MicroPython at /dev/cu.usbmodem101
Use Ctrl-] or Ctrl-x to exit this shell
>>> import button
```

## Sensors - ESP32-C3

```
mpremote fs cp sensors.py :sensors.py
mpremote repl
```

```
Connected to MicroPython at /dev/cu.usbmodem101
Use Ctrl-] or Ctrl-x to exit this shell
>>> import sensors
```

## Buzzer - ESP32-C3

Requires buzzer module.

```
mpremote fs cp buzzer.py :buzzer.py
mpremote repl
```

```
Connected to MicroPython at /dev/cu.usbmodem101
Use Ctrl-] or Ctrl-x to exit this shell
>>> import buzzer
```

## Lights - ESP32-C3

Requires RGB LED module.

```
mpremote fs cp lights.py :lights.py
mpremote repl
```

```
Connected to MicroPython at /dev/cu.usbmodem101
Use Ctrl-] or Ctrl-x to exit this shell
>>> import lights
```
