import smbus2
import PyNAU7802
import time

bus = smbus2.SMBus(1)
scale = PyNAU7802.NAU7802()
scale.begin(bus)

start_time = time.time()
while True:
    while not scale.available():
        pass
    weight = scale.getReading()

    print(f"{time.time() - start_time:.3f} {weight}")
