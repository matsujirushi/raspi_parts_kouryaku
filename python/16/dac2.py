import pigpio
import time

pi = pigpio.pi()
h = pi.spi_open(0, 20000000, 0)

while True:
  for i in range(100):
    val = int(i / 100 * 3 / 4.096 * 4096)
    val_bytes = val.to_bytes(2, 'big')
    pi.spi_write(h, [(0b0001 << 4) | val_bytes[0], val_bytes[1]])
    time.sleep(0.001)
