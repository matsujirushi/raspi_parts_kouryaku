import pigpio
import time

I2C_INTERFACE = 1
GP2Y0E03_ADDRESS = 0x40
SIGNAL_ACCUMULATION_NUMBER = 10

pi = pigpio.pi()

h = pi.i2c_open(I2C_INTERFACE, GP2Y0E03_ADDRESS)

pi.i2c_write_byte_data(h, 0xef, 0x00)   # Bank 0
pi.i2c_write_byte_data(h, 0xec, 0xff)   # Manual Clock
time.sleep(4 * (SIGNAL_ACCUMULATION_NUMBER + 10) / 1000)
(data_size, data) = pi.i2c_read_i2c_block_data(h, 0x64, 2)  # AE
ae = data[0] * 256 + data[1]
data = pi.i2c_read_byte_data(h, 0x67)   # AG
ag = 2 ** (data // 16) * ((data % 16 + 16) / 16)

pi.i2c_write_byte_data(h, 0x03, 0x00)   # Hold
time.sleep(2 * (SIGNAL_ACCUMULATION_NUMBER + 10) / 1000)
pi.i2c_write_byte_data(h, 0x4c, 0x10)   # Access to SRAM
time.sleep(2 * (SIGNAL_ACCUMULATION_NUMBER + 10) / 1000)
pi.i2c_write_byte_data(h, 0x90, 0x10)   # Low Level
pi.i2c_write_byte(h, 0x00)
(data_size, data_l) = pi.i2c_read_device(h, 220)
pi.i2c_write_byte_data(h, 0x90, 0x11)   # Middle Level
pi.i2c_write_byte(h, 0x00)
(data_size, data_m) = pi.i2c_read_device(h, 220)
pi.i2c_write_byte_data(h, 0x90, 0x12)   # High Level
pi.i2c_write_byte(h, 0x00)
(data_size, data_h) = pi.i2c_read_device(h, 220)
pi.i2c_write_byte_data(h, 0x90, 0x00)   # Disable
pi.i2c_write_byte_data(h, 0x03, 0x01)   # Normal

profile = []
for i in range(220):
    profile.append(8 / ag * 295 / ae * (data_h[i] * 65536 + data_m[i] * 256 + data_l[i]))

print(ae)
print(ag)
for i in range(220):
    print(profile[i])
