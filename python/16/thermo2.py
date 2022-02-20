import pigpio
import time

pi = pigpio.pi()
h = pi.spi_open(0, 5000000, 0)

while True:
  val =  pi.spi_read(h, 2)
  temp = (int.from_bytes(val[1], 'big', signed = True) >> 2) / 4
  print('temp = {0:.1f}'.format(temp))
  time.sleep(1)
