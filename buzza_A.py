# Your PICO can make annoying sounds using an inexpesnsive buzzer
# The buzzer used in this demo is:
# Adafruit  Buzzer 5V - Breadboard friendly Product ID: 1536
# With power applied it will oscilate at 2kHz making it very easy to control
#

import machine  # type: ignore
import utime  # type: ignore

buzzer = machine.Pin(15, machine.Pin.OUT)


def Buzzer_bee():
    buzzer.value(1)
    utime.sleep(1)
    buzzer.value(0)
    print("BEEEEEEEEEEEEE!")


while True:
    print("0: buzzer off\n1: buzzer on")

    Buzzer_option = "1"

    if Buzzer_option == "1":
        Buzzer_bee()
        print("buzzer ON")

    else:
        buzzer.value(0)
        print("buzzer OFF")
        
