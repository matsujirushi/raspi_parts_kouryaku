from luma.core.interface.serial import spi
from luma.oled.device import ssd1331
from luma.core.render import canvas
from PIL import ImageFont

device = ssd1331(spi())

font = ImageFont.truetype("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf", 10, encoding='unic')

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="navy", fill="fuchsia", width=4)
    draw.text((14, 20), "ラズパイマガジン", fill="yellow", font=font)
    draw.text((20, 30), "2021年秋号", fill="red", font=font)

while True:
    None
