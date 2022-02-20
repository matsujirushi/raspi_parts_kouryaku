import pigpio
import time
import struct

I2C_INTERFACE = 1
SRF02_ADDRESS = 0x70

pi = pigpio.pi()

h = pi.i2c_open(I2C_INTERFACE, SRF02_ADDRESS)

while True:
    pi.i2c_write_byte_data(h, 0, 0x52) # Real Ranging Mode - Result in micro-seconds
    time.sleep(70 / 1000)

    (data_size, data) = pi.i2c_read_i2c_block_data(h, 2, 2)
    val = struct.unpack('>H', data)[0]
    distance = 340 * 1000 * (val / 1000000) / 2
    print(distance)

    time.sleep(1)
