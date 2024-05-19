from machine import Pin
import time
from time import sleep
red=Pin(6,Pin.OUT)
yellow=Pin(7,Pin.OUT)
green=Pin(8,Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
while True:
    print(button.value())
    time.sleep(.5)
    if button.value()==1:
        red.on()
        sleep(2)
        yellow.on()
        sleep(.5)
        red.off()
        sleep(.4)
        yellow.off()
        green.on()
        sleep(2)
        yellow.on()
        sleep(.5)
        green.off()
        sleep(.5)
        yellow.off()
        red.on()
        sleep(1)
        red.off()
    else:
        red.value(0)
        yellow.value(0)
        green.value(0)
   