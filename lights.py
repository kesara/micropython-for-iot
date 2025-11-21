from neopixel import NeoPixel
from machine import Pin
from random import randint
from utime import sleep_ms

DELAY = 1000

led = Pin(8, Pin.OUT)
light = Pin(0, Pin.OUT)
np = NeoPixel(light, 1)

led.value(1)
sleep_ms(DELAY)
led.value(0)
sleep_ms(DELAY)

while True:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    np[0] = (r, g, b)
    np.write()
    sleep_ms(DELAY)
