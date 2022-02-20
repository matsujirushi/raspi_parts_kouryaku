import pigpio
import time

pi = pigpio.pi()
h = pi.i2c_open(1, 0x1D)
pi.i2c_write_byte_data(h, 0x2D, 0x08)

while True:
  val = pi.i2c_read_i2c_block_data(h, 0x32, 6)
  x_l = val[1][0]
  x_h = val[1][1]
  y_l = val[1][2]
  y_h = val[1][3]
  z_l = val[1][4]
  z_h = val[1][5]
  x = int.from_bytes([x_l, x_h], 'little', signed=True)
  y = int.from_bytes([y_l, y_h], 'little', signed=True)
  z = int.from_bytes([z_l, z_h], 'little', signed=True)
  print('{:.2f}, {:.2f}, {:.2f}'.format(x * 2.0 / 2 ** (10 - 1), y * 2.0 / 2 ** (10 - 1), z * 2.0 / 2 ** (10 - 1)))
  time.sleep(1)
