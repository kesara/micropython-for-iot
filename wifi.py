from machine import Pin
from utime import sleep_ms

import network
import urequests

LED = Pin("LED", Pin.OUT)
DELAY = 1000
SSID = "rp2-pico"
PASSWORD = "kiwipycon"


def connect():
    connection = network.WLAN(network.STA_IF)
    connection.active(True)
    connection.ifconfig(
        [
            "192.168.2.147",
            "255.255.255.0",
            "192.168.2.1",
            "9.9.9.9",
        ]
    )
    connection.connect(SSID, PASSWORD)
    while connection.status() != network.STAT_GOT_IP:
        # blink LED while connecting
        LED.value(1)
        sleep_ms(DELAY)
        LED.value(0)
        sleep_ms(DELAY)


def main():
    connect()

    response = urequests.get("http://ip.jsontest.com/")
    print(response.text)
    response = urequests.get("http://date.jsontest.com/")
    print(response.text)


if __name__ == "__main__":
    main()
