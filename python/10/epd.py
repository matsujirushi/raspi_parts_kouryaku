import os
import sys
from PIL import Image

LIBDIR = "/home/pi/e-Paper/RaspberryPi_JetsonNano/python/lib"

if os.path.exists(LIBDIR):
    sys.path.append(LIBDIR)
from waveshare_epd import epd2in13bc

epd = epd2in13bc.EPD()
epd.init()

black_image = Image.open(os.path.join(os.path.dirname(__file__), "raspimag-b.bmp"))
yellow_image = Image.open(os.path.join(os.path.dirname(__file__), "raspimag-y.bmp"))
epd.display(epd.getbuffer(black_image), epd.getbuffer(yellow_image))
