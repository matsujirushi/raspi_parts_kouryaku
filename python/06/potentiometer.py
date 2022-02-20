import pigpio
import time

INTERVAL = 0.1


def read_adc_ch0(pi, h):
    count, data = pi.spi_xfer(h, [0b01101000, 0])
    return int.from_bytes([data[0] & 0x03, data[1]], 'big') / 1023


pi = pigpio.pi()
h = pi.spi_open(0, 1000000, 0)

try:
    while True:
        print(read_adc_ch0(pi, h) * 3.3)
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    pass

pi.spi_close(h)
pi.stop()
