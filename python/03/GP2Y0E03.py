import pigpio
import time

I2C_INTERFACE = 1
GP2Y0E03_ADDRESS = 0x40

pi = pigpio.pi()

h = pi.i2c_open(I2C_INTERFACE, GP2Y0E03_ADDRESS)

shift_bit = pi.i2c_read_byte_data(h, 0x35) & 0x07

while True:
    (data_size, data) = pi.i2c_read_i2c_block_data(h, 0x5e, 2)
    print((data[0] * 16 + data[1] % 16) / (16 * 2 ** shift_bit) * 10)

    time.sleep(1)
