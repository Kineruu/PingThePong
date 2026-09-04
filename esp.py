from machine import Pin
import time

#todo:
# add a schematic for each wire and connection
# make somewhat reasonable breadboard prototype
# make it either player vs bot or player vs player
# maybe document the entire thing like what i did and what parts i used

info = 0

# Left Paddle
b1 = Pin(11, Pin.IN, Pin.PULL_UP) # W
b2 = Pin(14, Pin.IN, Pin.PULL_UP) # A
b3 = Pin(13, Pin.IN, Pin.PULL_UP) # S
b4 = Pin(12, Pin.IN, Pin.PULL_UP) # D

# Right paddle
r1 = Pin(4, Pin.IN, Pin.PULL_UP) # ↑
r2 = Pin(5, Pin.IN, Pin.PULL_UP) # ←
r3 = Pin(7, Pin.IN, Pin.PULL_UP) # ↓
r4 = Pin(6, Pin.IN, Pin.PULL_UP) # →

while True:
    if info == 1:
        print("---------------")
        print("L1: ", b1.value()) # W
        print("L2: ", b2.value()) # A
        print("L3: ", b3.value()) # S
        print("L4: ", b4.value()) # D
        print("---------------")
        print("R1: ", r1.value()) # ↑
        print("R2: ", r2.value()) # ←
        print("R3: ", r3.value()) # ↓
        print("R4: ", r4.value()) # →

    

    time.sleep_ms(100)
    