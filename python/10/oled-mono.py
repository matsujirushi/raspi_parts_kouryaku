from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
import random
import time

device = ssd1306(i2c())

while True:
    with canvas(device) as draw:
        for i in range(3):
            box = [random.randrange(device.width), random.randrange(device.height), random.randrange(device.width), random.randrange(device.height)]
            draw.rectangle(box, outline="white", fill="black", width=1)

    time.sleep(1)
