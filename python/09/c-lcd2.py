import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
import time

GPIO.setwarnings(False)
display = CharLCD(numbering_mode=GPIO.BOARD, pin_rs=7, pin_rw=11, pin_e=13, pins_data=[29, 31, 33, 35], cols=16, rows=2)
display.cursor_mode = "blink"

while True:
    display.cursor_pos = (0, 0)
    for c in "RasPi Magazine":
        display.write_string(c)
        time.sleep(0.2)
    time.sleep(2)

    display.cursor_pos = (1, 3)
    for c in "Summer - 2021":
        display.write_string(c)
        time.sleep(0.2)
    time.sleep(2)

    display.clear()
    time.sleep(2)
