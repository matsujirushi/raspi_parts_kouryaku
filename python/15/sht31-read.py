import pigpio
import time

pi = pigpio.pi()
h = pi.i2c_open(1, 0x45)

while True:
  pi.i2c_write_device(h, [0x2c, 0x10])
  
  while True:
    result = pi.i2c_read_device(h, 6)
    if result[0] >= 0:
      break
  
  if result[0] == 6:
    temp = -45 + 175 * int.from_bytes(result[1][0:2], 'big') / 65535
    humi = 100 * int.from_bytes(result[1][3:5], 'big') / 65535
    print('temp = {:.1f}, humi = {:.1f}'.format(temp, humi))

  time.sleep(1)
