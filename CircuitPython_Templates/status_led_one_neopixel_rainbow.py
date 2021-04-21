"""
CircuitPython status NeoPixel rainbow example.

Update PIXELBUF_VERSION to _pixelbuf if available for the board (this is the most common case!)
or to adafruit_pypixelbuf where necessary (typically non-Express SAMD21 M0 boards).

For example:
If you are using a QT Py RP2040, change PIXELBUF_VERSION to _pixelbuf.
If you are using a QT Py M0, change PIXELBUF_VERSION to adafruit_pypixelbuf.
"""
import time
import board
import neopixel
from PIXELBUF_VERSION import colorwheel

pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write=False)

pixel.brightness = 0.3


def rainbow(speed):
    for j in range(255):
        for i in range(1):
            pixel_index = (i * 256 // 1) + j
            pixel[i] = colorwheel(pixel_index & 255)
        pixel.show()
        time.sleep(speed)


while True:
    rainbow(0.02)
