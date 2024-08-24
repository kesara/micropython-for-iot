from machine import Pin, ADC
from utime import sleep_ms

LED = Pin("LED", Pin.OUT)
DELAY = 1000


def get_temp():
    adc = ADC(ADC.CORE_TEMP)
    adc_voltage = adc.read_u16() * 3.3 / 65535
    temp = round(27 - (adc_voltage - 0.706) / 0.001721, 1)
    return temp


while True:
    print(f"{get_temp()}° C")
    LED.value(1)
    sleep_ms(DELAY)
    LED.value(0)
    sleep_ms(DELAY)
