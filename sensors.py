from machine import Pin, ADC
from utime import sleep_ms, ticks_ms, ticks_diff

DELAY = 1000

led = Pin(8, Pin.OUT)
adc = ADC(0)


def get_sound_level():
    start = ticks_ms()
    sample_min = 2**16
    sample_max = 0

    while ticks_diff(ticks_ms(), start) < 50:
        level = adc.read_u16()
        if level < sample_min:
            sample_min = level
        if level > sample_max:
            sample_max = level
        print_level("MIN", sample_min)
        print_level("CUR", level)
        print_level("MAX", sample_max)


def print_level(label, value):
    level = "["
    for i in range(0, int(value) / 1000):
        level += "="
    print(f"{label} {level}>")


while True:
    led.value(1)
    sleep_ms(DELAY)
    led.value(0)
    sleep_ms(DELAY)
    get_sound_level()
