from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

device = ssd1306(i2c())

font = ImageFont.truetype("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf", 10, encoding='unic')

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black", width=4)
    draw.text((28, 20), "ラズパイマガジン", fill="white", font=font)
    draw.text((36, 30), "2021年秋号", fill="white", font=font)

while True:
    None
