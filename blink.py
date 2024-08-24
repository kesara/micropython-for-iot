from machine import Pin
from utime import sleep_ms

LED = Pin("LED", Pin.OUT)
DELAY = 1000

while True:
    LED.value(1)
    sleep_ms(DELAY)
    LED.value(0)
    sleep_ms(DELAY)
