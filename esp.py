from machine import Pin
import time

#todo:
# definitely fix the l and r buttons
# add a schematic for each wire and connection
# make somewhat reasonable breadboard prototype
# make it either player vs bot or player vs player
# maybe document the entire thing like what i did and what parts i used

# Left paddle
L_B1 = Pin(1, Pin.IN, Pin.PULL_UP)
L_B2 = Pin(2, Pin.IN, Pin.PULL_UP)
L_B3 = Pin(44, Pin.IN, Pin.PULL_UP)
L_B4 = Pin(43, Pin.IN, Pin.PULL_UP)

# Right paddle
#R_B1 = Pin(1, Pin.IN, Pin.PULL_UP)
#R_B2 = Pin(1, Pin.IN, Pin.PULL_UP)
#R_B3 = Pin(1, Pin.IN, Pin.PULL_UP)
#R_B4 = Pin(1, Pin.IN, Pin.PULL_UP)

while True:
    b1_value = L_B1.value()
    b2_value = L_B2.value()
    b3_value = L_B3.value()
    b4_value = L_B4.value()

    print("---------------")
    print("B1: ", b1_value)
    print("B2: ", b2_value)
    print("B3: ", b3_value)
    print("B4: ", b4_value)
    time.sleep_ms(500)

    