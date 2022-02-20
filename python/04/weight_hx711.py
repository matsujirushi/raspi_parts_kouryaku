import RPi.GPIO as GPIO
from hx711 import HX711
import time

SAMPLING_NUMBER = 1

GPIO.setmode(GPIO.BCM)
scale = HX711(dout_pin=5, pd_sck_pin=6)

start_time = time.time()
while True:
    weight = scale.get_raw_data_mean(SAMPLING_NUMBER)

    print(f"{time.time() - start_time:.3f} {weight}")
