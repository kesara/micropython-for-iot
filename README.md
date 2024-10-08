# MicroPython for Internet of Things - Kiwi PyCon XIII

Kiwi PyCon XIII workshop that explores the use of MicroPython on a Raspberry Pi Pico board in an Internet of Things context. Dr Glenn Ramsey conducted the workshop.

## Hardware
* [RasberryPi Pico WH](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#raspberry-pi-pico-w-and-pico-wh)
* [KY-038 Sound Detection Module](https://www.datasheethub.com/ky-038-lm393-sound-detection-module/)

## Documentation
* [MicroPython documentation](https://docs.micropython.org/)

## Getting Started
* Create a new Python venv

```
python3 -m venv venv
./activate
```

*  Install `mpremote`.
```
pip install mpremote
```

*  Download and copy [MicroPython for Raspberry Pi Pico W with Wi-Fi and Bluetooth LE support](https://www.raspberrypi.com/
documentation/microcontrollers/micropython.html).

```
cp RPI_PICO_W-20240602-v1.23.0.uf2 /Volumes/RPI-RP2/
```

* Test `mpremote` access.
```
mpremote help
mpremote devs # list connected devices
mpremote repl # Python shell. Press `Ctrl` + `b`.
```

## Blink

```
mpremote fs cp blink.py :blink.py
mpremote repl
```

```
MicroPython v1.23.0 on 2024-06-02; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> import blink
```

## WiFi

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

## Temperature

```
mpremote fs cp temp.py :temp.py
mpremote repl
```

```
MicroPython v1.23.0 on 2024-06-02; Raspberry Pi Pico W with RP2040
Type "help()" for more information.
>>> import temp
```
