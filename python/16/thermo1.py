import pigpio
import time

pi = pigpio.pi()
h = pi.spi_open(0, 5000000, 0)

while True:
  val =  pi.spi_read(h, 4)
  temp = (int.from_bytes(val[1][0:2], 'big', signed = True) >> 2) / 4
  int_temp = (int.from_bytes(val[1][2:4], 'big', signed = True) >> 4) / 16
  print('temp = {0:.1f}, int_temp = {1:.1f}'.format(temp, int_temp))
  time.sleep(1)
