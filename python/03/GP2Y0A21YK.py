import pigpio
import time

pi = pigpio.pi()
h = pi.spi_open(0, 1000000, 0)

while True:
  val = pi.spi_xfer(h, [0b01101000, 0])

  volt = int.from_bytes([val[1][0] & 0x03, val[1][1]], 'big') * 3.3 / 1023
  print(volt * 3 / 2)

  time.sleep(1)
