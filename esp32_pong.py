from machine import Pin
import time

p = Pin(11, Pin.IN, Pin.PULL_UP)

while True:
    print(p.value())
    time.sleep_ms(500)