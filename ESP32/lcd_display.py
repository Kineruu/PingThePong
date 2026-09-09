# Settings and code for my LCD screen - hardware configuration

from machine import Pin, SPI
from ili9341 import Display

# Waveshare 2.4" ILI9341 LCD
# DIN  -> GPIO 5
# CLK  -> GPIO 6
# CS   -> GPIO 7
# DC   -> GPIO 15
# RST  -> GPIO 16

spi = SPI(
    1,
    baudrate=20_000_000,
    polarity=0,
    phase=0,
    sck=Pin(6),
    mosi=Pin(5)
)

display = Display(
    spi,
    cs=Pin(7),
    dc=Pin(15),
    rst=Pin(16),
    width=240,
    height=320,
    rotation=0
)