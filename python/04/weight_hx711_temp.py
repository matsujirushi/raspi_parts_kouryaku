import RPi.GPIO as GPIO
from hx711 import HX711
import time
import pigpio

SAMPLING_NUMBER = 1

GPIO.setmode(GPIO.BCM)
scale = HX711(dout_pin=5, pd_sck_pin=6)
pi = pigpio.pi()
sht31 = pi.i2c_open(1, 0x45)

start_time = time.time()
while True:
    weight = scale.get_raw_data_mean(SAMPLING_NUMBER)

    pi.i2c_write_device(sht31, [0x24, 0x00])
    time.sleep(0.015)
    (val_count, val) = pi.i2c_read_device(sht31, 2 + 1 + 2 + 1)
    temp = -45 + 175 * int.from_bytes(val[0:2], 'big', signed=False) / 65535

    print(f"{time.time() - start_time:.3f} {weight} {temp}")
