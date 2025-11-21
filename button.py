from machine import Pin
from micropython import schedule
from random import randint
from utime import sleep_ms

import gc
import network
import urequests

DELAY = 1000
SSID = "upycon"
PASSWORD = "kiwipycon"
URL = "http://192.168.2.64:8000/"

led = Pin(8, Pin.OUT)
button = Pin(9, Pin.IN, Pin.PULL_UP)


def connect():
    connection = network.WLAN(network.STA_IF)
    connection.active(True)
    connection.ifconfig(
        [
            "192.168.2.185",
            "255.255.255.0",
            "192.168.2.1",
            "9.9.9.9",
        ]
    )
    connection.connect(SSID, PASSWORD)
    while connection.status() != network.STAT_GOT_IP:
        # blink LED while connecting
        led.value(0)
        sleep_ms(DELAY)
        led.value(1)
        sleep_ms(DELAY)


def blink(loops):
    for i in range(0, loops):
        led.value(not led.value())
        sleep_ms(DELAY)


def get_colour():
    return f"{randint(0, 255):0.2x}"


def send_data(name):
    r = get_colour()
    g = get_colour()
    b = get_colour()
    data = {"text": f"{name}", "color": f"#{r}{g}{b}"}
    urequests.post(URL, json=data)
    gc.collect()


def button_click():
    old_state = 1
    while True:
        new_state = button.value()

        if new_state == 0 and old_state == 1:
            # button pressed
            print(new_state)
            print(old_state)
            led.value(not led.value())
            schedule(send_data, "K")

        old_state = new_state
        sleep_ms(DELAY)


def main():
    print("connecting..")
    connect()
    print("connected..")

    # response = urequests.get("https://api.seeip.org/jsonip")
    # print(response.text)

    blink(2)

    send_data("Kesara")

    button_click()


main()
