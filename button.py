from machine import Pin
from utime import sleep_ms

DELAY = 1000

led = Pin(8, Pin.OUT)
button = Pin(9, Pin.IN, Pin.PULL_UP)
led_value = 0

while True:
    if button.value() == 0:
        # button press
        if led_value == 0:
            led_value = 1
        else:
            led_value = 0
    led.value(led_value)
    sleep_ms(DELAY)
