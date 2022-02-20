import board
import busio
import adafruit_so1602
import time

i2c = busio.I2C(board.SCL, board.SDA)
display = adafruit_so1602.Adafruit_SO1602_I2C(i2c)

while True:
    display.writeLine("RasPi Magazine")
    time.sleep(2)

    display.writeLine("Summer - 2021", 1)
    time.sleep(2)

    display.displayClear()
    time.sleep(2)
