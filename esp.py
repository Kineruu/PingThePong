from machine import Pin
import time

#todo:
# add a schematic for each wire and connection
# make somewhat reasonable breadboard prototype
# make it either player vs bot or player vs player
# maybe document the entire thing like what i did and what parts i used

# Left Paddle
L_buttons = [
    Pin(1, Pin.IN, Pin.PULL_UP),
    Pin(2, Pin.IN, Pin.PULL_UP),
    Pin(44, Pin.IN, Pin.PULL_UP),
    Pin(43, Pin.IN, Pin.PULL_UP)
]

Settings_buttons = [
    #Pin() Quit
    #Pin() Stop? Pause?
    #Pin() Player vs Player
    #Pin() Player vs Bot
    #Pin() Bot vs Bot?  
]

# Right paddle
R_buttons = [
    #Pin(),
    #Pin(),
    #Pin(),
    #Pin()
]

while True:
    L_values = [button.value() for button in L_buttons]
    #R_values = [button.value() for button in R_buttons]

    print("Left: ", L_values)
    #print("Right:", R_values)

    time.sleep_ms(250)

    